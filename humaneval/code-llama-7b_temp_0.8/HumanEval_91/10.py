
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
    punct = [".", "?", "!"]
    if not S:
        return 0
    if S[0] != "I":
        return 0
    if S[-1] in punct:
        return 1
    else:
        return 1 + is_bored(S[S.index(punct[0]) + 1 :])

