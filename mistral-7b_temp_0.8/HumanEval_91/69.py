
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
    bore = 0
    i = 0
    for x in S:
        if i == 0:
            if x == "I":
                i = 1
                continue
            else:
                i = 0
                continue
        else:
            if x == ".":
                i = 0
                continue
            elif x == "?":
                i = 0
                continue
            elif x == "!":
                i = 0
                continue
            else:
                i = 0
                continue
    return bore
