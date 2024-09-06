
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
    is_bored_counter = 0
    index = 0
    while index < len(S):
        if S[index:].find('I') == 0:
            if S[index + 1:].find('.') != -1 or S[index + 1:].find('?') != -1 or S[index + 1:].find('!') != -1:
                is_bored_counter += 1
        index += 1
    return is_bored_counter

