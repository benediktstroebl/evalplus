
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
    # Create a set to keep track of unique words
    word_set = set()
    # Create a set to keep track of words that start with "I"
    word_set_i = set()
    # Create a set to keep track of words that end with "ing"
    word_set_ing = set()
    # Iterate through the string of words
    for word in S:
        # Check if the word is in the word_set
        if word in word_set:
            return 0
        # Check if the word starts with "I"
        if word[0] == 'I':
            word_set_i.add(word)
        # Check if the word ends with "ing"
        if word.endswith("ing"):
            word_set_ing.add(word)
    # If none of the above conditions were met, it means that the word doesn't
    # belong to any of the sets, so we return the number of boredoms
    return len(word_set_i) + len(word_set_ing)