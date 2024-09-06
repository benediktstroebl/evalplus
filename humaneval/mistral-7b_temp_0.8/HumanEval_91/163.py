
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
    while i < len(S):
        if S[i] == 'I':
            j = i
            while j < len(S) - 1 and S[j+1] != '.' and S[j+1] != '?' and S[j+1] != '!':
                j += 1
            if j != i and j + 1 < len(S) and S[j+1] in '?.':
                i = j + 1
            else:
                i += 1
        else:
            i += 1
    return i - 1

