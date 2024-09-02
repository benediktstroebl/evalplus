
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

    count = 0
    for c in S:
        if c == '.' or c == '?' or c == '!':
            count += is_bored(S[S.index(c):])
            return count
        if c == 'I':
            count += 1
    return count
