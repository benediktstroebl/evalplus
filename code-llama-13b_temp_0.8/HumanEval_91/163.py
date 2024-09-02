
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
    sentences = S.split('.')
    sentences.append('')
    bored = False
    boredom_count = 0
    
    for sentence in sentences:
        if bored:
            if sentence.strip():
                boredom_count += 1
        if sentence.strip().startswith('I'):
            bored = True
    return boredom_count
