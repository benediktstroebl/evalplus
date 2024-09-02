
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
    
    word = "I"
    boredoms = 0
    for char in S:
        if char == "." or char == "?" or char == "!":
            boredoms += 1
        if char == "I":
            if S[S.find(word) + 1] == "I":
                boredoms += 1
            word = S[S.find(word) + 1]
    return boredoms

