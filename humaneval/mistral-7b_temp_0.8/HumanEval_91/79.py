
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
    bored = 0
    for i in range(len(S)):
        if S[i].isupper() and S[i] != 'I':
            continue
        elif S[i].isalpha() and S[i] == 'I':
            if i == 0 or (S[i - 1] == '!' or S[i - 1] == '.' or S[i - 1] == '?'):
                bored += 1
    return bored

