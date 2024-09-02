
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    if S.count('.') < 2:
        return 0

    prev_char = None
    curr_state = False
    n_bored = 0
    for char in S:
        if prev_char in {'.', '?', '!'}:
            curr_state = False
            n_bored = 0
        if char == 'I':
            curr_state = True
        prev_char = char
        if curr_state:
            n_bored += 1

    return n_bored
