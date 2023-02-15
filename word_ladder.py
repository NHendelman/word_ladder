#!/bin/python3


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):

    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony',
    'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output (edit for push)
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots',
    'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    '''
    Create a stack
    Push the start word onto the stack
    Create a queue
    Enqueue the stack onto the queue

    While the queue is not empty
        Dequeue a stack from the queue
        For each word in the dictionary
            If the word is adjacent to the top of the stack
                If this word is the end word
                    You are done!
                    The front stack plus this word is your word ladder.
                Make a copy of the stack
                Push the found word onto the copy
                Enqueue the copy
                Delete word from the dictionary
    '''
    from collections import deque
    import copy

    with open('words5.dict', 'r') as f:
        text = f.read()
    words = text.split()
    if start_word not in words or end_word not in words:
        return None
    if len(start_word) != 5 or len(end_word) != 5:
        return None
    if start_word == end_word:
        return [start_word]

    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)

    while len(queue) != 0:
        ladder = queue.popleft()
        for word in list(words):
            if _adjacent(ladder[-1], word):
                if word == end_word:
                    ladder.append(word)
                    return ladder
                newstack = copy.copy(ladder)
                newstack.append(word)
                queue.append(newstack)
                words.remove(word)
    return None


def _adjacent(word1, word2):

    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''

    if len(word1) == len(word2):
        num_diffs = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                num_diffs += 1
        if num_diffs <= 1:
            return True
        return False


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''

    verify = 0
    if not ladder:
        return False
    if len(ladder) == 1:
        verify = True
    for word in range(len(ladder) - 1):
        if not _adjacent(ladder[word], ladder[word + 1]):
            return False
        else:
            verify = True
    return verify
