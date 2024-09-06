
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
    
    start = S.find("I")
    while start!= -1:
        end = S[start:].find(".")
        if end == -1:
            end = S[start:].find("?")
        if end == -1:
            end = S[start:].find("!")
        if end == -1:
            return 1
        else:
            start = S[start:].find("I")
    
    return 0
