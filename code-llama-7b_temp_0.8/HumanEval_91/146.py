
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

    # The number of boredom
    bored = 0

    # Start at index 0
    index = 0

    # Loop through string
    while index < len(S):
        # Find the next sentence delimiter
        delimiter = S.find('.', index)
        if delimiter == -1:
            delimiter = S.find('!', index)
            if delimiter == -1:
                delimiter = S.find('?', index)

        # If no delimiter, then the string is over
        if delimiter == -1:
            break

        # The sentence is everything between the current index and the delimiter
        sentence = S[index:delimiter]

        # If the sentence starts with "I", it's bored
        if sentence.startswith('I '):
            bored += 1

        # Move to the next delimiter
        index = delimiter + 1

    return bored

