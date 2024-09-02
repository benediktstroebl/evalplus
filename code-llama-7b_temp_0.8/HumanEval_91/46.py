
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
    result = 0
    sentence = []
    for c in S:
        if c.isalpha():
            sentence.append(c.lower())
        elif c in ".?!" and sentence:
            sentence[0] == "i" and result += 1
            sentence.clear()

    sentence[0] == "i" and result += 1
    return result
