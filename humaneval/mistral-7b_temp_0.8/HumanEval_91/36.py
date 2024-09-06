
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
    i = 0
    while i < len(S):
        if S[i:i+2] == 'I ':
            i += 2
            if i == len(S):
                count += 1
            else:
                if S[i] == '.' or S[i] == '!' or S[i] == '?':
                    count += 1
                    i += 1
                else:
                    i += 1
        else:
            i += 1
    return count
