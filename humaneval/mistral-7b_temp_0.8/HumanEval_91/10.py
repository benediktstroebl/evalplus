
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
    bored_count = 0
    i = 0
    while i < len(S):
        if S[i] == 'I':
            while i < len(S) and (S[i] != '.' or S[i] != '?' or S[i] != '!'):
                i += 1
            bored_count += 1
        i += 1
    return bored_count


