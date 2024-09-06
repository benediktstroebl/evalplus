
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
        # Skip all non-alphanumeric characters
        while not S[i].isalnum():
            i += 1
        # Skip all alphanumeric characters
        while S[i].isalnum():
            i += 1
        if S[i] == 'I':
            count += 1
        # Skip to the next sentence
        if S[i] in ('.', '?', '!'):
            i += 1
    return count

