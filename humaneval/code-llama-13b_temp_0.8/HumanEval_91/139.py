
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
    count = 0
    for s in S:
        if s == ".":
            count = count + 1 if count > 0 else 0
        elif s == "?" or s == "!":
            count = 0
        elif s == "I":
            count = count + 1 if count == 0 else count
    return count

