
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
    # ...
    counter = 0
    i = 0
    while i < len(S):
        j = i + 1
        if j == len(S):
            break
        while S[j] != "." and S[j] != "?" and S[j] != "!":
            j += 1
        if S[i:j] == "I":
            counter += 1
        i = j
    return counter
