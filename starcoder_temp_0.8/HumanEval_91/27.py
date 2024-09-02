
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
    n_bored = 0
    if "." in S or "?" in S or "!" in S:
        if S[0:2] == "I ":
            n_bored += 1
            while "I " in S:
                S = S[S.find("I ")+2:]
    return n_bored
