
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
    if len(S) == 0:
        return 0
    count = 0
    word = ""
    for c in S:
        if c == " ":
            if word == "I":
                count += 1
            word = ""
        elif c in ".?!":
            if word == "I":
                count += 1
            word = ""
        else:
            word += c
    return count

