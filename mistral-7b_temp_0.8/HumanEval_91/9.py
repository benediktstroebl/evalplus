
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
    # your code here
    I = 0
    # this is a fix for the "I'm" example:
    # if S[0] == "I" and S[1] == "m":
    #     I += 1
    #     S = S[2:]
    #
    # while "." in S:
    #     if S[0] == "I":
    #         I += 1
    #     S = S[1:]
    #
    # while "?" in S:
    #     if S[0] == "I":
    #         I += 1
    #     S = S[1:]
    #
    # while "!" in S:
    #     if S[0] == "I":
    #         I += 1
    #     S = S[1:]
    #
    # return I

    return len(S.split("I")[1:])
