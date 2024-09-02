
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
    start = 0
    end = len(S) - 1

    while start <= end:
        if S[start] == 'I':
            bored += 1
            for i in range(start, end):
                if S[i] == '.':
                    break
            start = i + 1
        else:
            start += 1

    return bored
