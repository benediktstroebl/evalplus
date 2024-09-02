
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

    
    boredoms = 0
    if S[0] == "I":
        boredoms += 1
    for i in range(len(S)-1):
        if S[i] == "." or S[i] == "?" or S[i] == "!":
            S = S[:i] + S[i+1:]
    boredoms += is_bored(S)
    return boredoms

