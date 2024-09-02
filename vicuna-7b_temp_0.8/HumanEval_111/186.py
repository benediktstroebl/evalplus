
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
    # split the string into a list of characters
    words = test.split()
    # initialize a dictionary to store the letter-count pairs
    word_count = {}
    # iterate over the words
    for word in words:
        # check if the word is in the dictionary
        if word in word_count:
            # if the word is in the dictionary, increment the count
            word_count[word] += 1
        else:
            # if the word is not in the dictionary, add it with a count of 1
            word_count[word] = 1
    # return the dictionary of letter-count pairs
    return word_count
