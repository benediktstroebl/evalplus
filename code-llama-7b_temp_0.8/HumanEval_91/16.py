
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
    count = 0
    start_sentence = 0
    end_sentence = 0
    for index, char in enumerate(S):
        # Look for the beginning of a sentence
        if char == "I":
            start_sentence = index
        # Look for the end of a sentence
        if char in [".", "?", "!"]:
            end_sentence = index
            if start_sentence < end_sentence:
                count += 1
    return count
