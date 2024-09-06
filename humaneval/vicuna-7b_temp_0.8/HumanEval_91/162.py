
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
    sent_idx = 0
    for idx, word in enumerate(S):
        if word.startswith("I"):
            sent_idx = idx + 1
            break
    else:
        return 0
    return len(S) - sent_idx
