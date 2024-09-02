
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
    if '.' in S:
        return S.count('I') + S.count('i') + S.count('a')
    if '!' in S:
        return S.count('i') + S.count('I') + S.count('a') + S.count('A')
    if '?' in S:
        return S.count('I') + S.count('i') + S.count('a') + S.count('A')
    return 0
