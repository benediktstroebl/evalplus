
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
    assert S, "You can't count boredoms for empty string."
    boredoms = 0
    sentence_delimiters = " .?!"
    for sentence in S.split(sentence_delimiters):
        if sentence.lower().startswith('i'):
            boredoms += 1
    return boredoms

