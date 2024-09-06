
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
    if S == "":
        return 0
    if S[0] == "I":
        return 1
    i = 0
    boredom_count = 0
    while i < len(S):
        c = S[i]
        if c == ".":
            if S[i-1] == "I":
                boredom_count += 1
        elif c == "?" or c == "!":
            if S[i-1] == "I":
                boredom_count += 1
            break
        i += 1
    return boredom_count
