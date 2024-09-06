
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
    if S == None or S == "":
        return 0
    
    count = 0
    if S[0] == "I":
        count += 1
    for ch in ['.', '?', '!']:
        if S.find(ch) != -1:
            count += (S.find(ch) + 1) == "I"
    return count
    
