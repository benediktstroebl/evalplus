
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
    # If the string is empty, the number of boredoms is 0
    if not S:
        return 0
    # Split the string into a list of words
    words = S.split()
    # Initialize the number of boredoms to 0
    boredoms = 0
    # Loop through the list of words
    for word in words:
        # If the word starts with the letter 'I' and there are
        # at least two more words in the list, then add 1 to the
        # number of boredoms
        if word[0].upper() == 'I' and len(words) > 2:
            boredoms += 1
    # Return the number of boredoms
    return boredoms
