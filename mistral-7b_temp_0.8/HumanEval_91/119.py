
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
    result = 0
    S = S.lower()
    for i in range(len(S)):
        if S[i] == 'i' and i != 0 and S[i-1] == ' ':
            result += 1
    return result
