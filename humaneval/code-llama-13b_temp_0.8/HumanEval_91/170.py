
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
    boredoms = 0
    boredom_started = False
    for i, letter in enumerate(S):
        if letter == '.' or letter == '?' or letter == '!':
            boredom_started = False
        if boredom_started and letter == 'I':
            boredoms += 1
        if letter == 'I':
            boredom_started = True
    return boredoms
