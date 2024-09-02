
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
    boredom = 0
    start = 0
    for i in range(len(S)):
        if S[i] in {'.', '!', '?'}:
            if start == i:
                boredom += 1
            else:
                start = i
        elif S[i] == 'I' and i > 0:
            if S[i - 1] == ' ' or S[i - 1] == '.':
                boredom += 1
            elif S[i - 1] == '.' or S[i - 1] == '!':
                start = i
    return boredom

