
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

    cnt = 0
    if not S:
        return cnt

    # List of chars that mark the end of a sentence
    end_chars = ['.', '?', '!']

    # State of the machine
    in_sentence = False
    for c in S:

        # Start of a new sentence
        if c in end_chars and in_sentence:
            cnt += 1
            in_sentence = False

        # End of a sentence
        if c in end_chars and not in_sentence:
            in_sentence = True

        # If a new sentence started and the first word is 'I', it's a boredom
        if c == 'I' and in_sentence:
            cnt += 1
            in_sentence = False

    return cnt
