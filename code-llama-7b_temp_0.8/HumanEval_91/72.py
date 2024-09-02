
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
    bored = 0
    current_sentence = ""
    for c in S:
        if c == '.':
            if current_sentence.startswith("I"):
                bored += 1
            current_sentence = ""
        else:
            current_sentence += c
    return bored
