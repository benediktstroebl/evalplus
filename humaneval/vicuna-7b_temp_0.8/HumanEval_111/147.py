
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
    # convert the string to a set of characters
    char_set = set(test)

    # create an empty dictionary to store the letter-count pairs
    hist = {}

    # loop through the characters in the set
    for char in char_set:
        # if the character is in the histogram, increment its count
        if char in hist:
            hist[char] += 1
        else:
            # if the character is not in the histogram, add it with a count of 1
            hist[char] = 1

    return hist
