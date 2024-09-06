
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
    sentence_count = 0
    sentence_length = 0
    for char in S:
        if char.isspace():
            sentence_length += 1
            if sentence_length == 1 and char == 'I':
                sentence_count += 1
            sentence_length = 0
    return sentence_count
