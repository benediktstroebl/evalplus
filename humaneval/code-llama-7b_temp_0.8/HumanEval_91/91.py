
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
    is_bored_count = 0
    sentence = ""
    for letter in S:
        if letter == '.' or letter == '?' or letter == '!':
            if sentence.find("I") == 0:
                is_bored_count += 1
            sentence = ""
        else:
            sentence += letter
    if sentence.find("I") == 0:
        is_bored_count += 1
    return is_bored_count
