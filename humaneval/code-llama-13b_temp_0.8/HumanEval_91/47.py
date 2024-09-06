
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
    bored_flag = False

    for word in S.split('.'):
        for char in word:
            if char == ' ':
                bored_flag = False
            elif char.lower() == 'i':
                bored_flag = True
        if bored_flag:
            bored_count += 1
    return bored_count
