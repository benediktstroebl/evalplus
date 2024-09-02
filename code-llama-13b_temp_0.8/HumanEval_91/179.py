
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
    sentence = True
    i = 0
    boredom_count = 0
    while sentence:
        try:
            i = S.index('.', i) + 1
            if i > 0:
                sentence = S[i] == 'I'
                boredom_count += sentence
        except:
            sentence = False
    return boredom_count
