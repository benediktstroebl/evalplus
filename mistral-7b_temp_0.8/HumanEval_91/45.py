
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
    i = 0
    count = 0
    while i < len(S):
        if S[i] == "I" and S[i+1] == " " and S[i+2] == "." or S[i+1] == "?" or S[i+1] == "!":
            count += 1
        i += 1
    return count

    # def is_bored(S):
    #     """
    #     You'll be given a string of words, and your task is to count the number
    #     of boredoms. A boredom is a sentence that starts with the word "I".
    #     Sentences are delimited by '.', '?' or '!'.
    #     For example:
    #     >>> is_bored("Hello world")
    #     0
    #     >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    #     1
    #     """
    #     return len([i for i,j in enumerate(S) if j == "I" and S[
