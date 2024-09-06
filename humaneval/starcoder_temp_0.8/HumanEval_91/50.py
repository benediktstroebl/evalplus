
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
    if type(S)!= str:
        raise TypeError("The argument must be a string")
    if len(S) == 0:
        return 0
    n_bored = 0
    for c in S:
        if c == "." or c == "?" or c == "!":
            n_bored += 1
        if c == "I":
            n_bored += 1
    return n_bored // 2
