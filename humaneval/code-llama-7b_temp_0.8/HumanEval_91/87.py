
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
    "*** YOUR CODE HERE ***"
    i = 0
    l = 0
    for c in S:
        if c == ".":
            if S[i:l] == "I":
                i = l + 1
            l += 1
        elif c == "?":
            if S[i:l] == "I":
                i = l + 1
            l += 1
        elif c == "!":
            if S[i:l] == "I":
                i = l + 1
            l += 1
        else:
            l += 1
    return i
