
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
    while True:
        if S[i] == 'I':
            j = i
            while True:
                if S[j] in ['.', '?', '!']:
                    return j - i + 1
                j += 1
        i += 1
