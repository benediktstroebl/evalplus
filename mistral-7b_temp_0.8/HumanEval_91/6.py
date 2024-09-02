
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
    # Your code here
    # we could use a regex to find the "i" word and split it into a list
    # of words, so we can count the length of the list,
    # but we're doing it the long way.
    sentence = S.split()
    word_count = 0
    for word in sentence:
        if word.lower() == "i":
            word_count += 1
    return word_count
    # pass
    # return 0

