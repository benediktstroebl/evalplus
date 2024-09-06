
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
    i = len(S) // 2
    while i >= 0:
        if S[i] == "I":
            j = 1
            while j < len(S) and S[i - j] != "." or S[i - j] != "!" or S[i - j] != "?":
                j += 1
            if j == len(S):
                break
        i -= 1
    return i

