
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
    # remove whitespace
    test = test.lower().strip()
    
    # initialize dictionary
    hist = {}
    
    # iterate through each character
    for char in test:
        # if the character is in the dictionary
        if char in hist:
            # increment the count
            hist[char] += 1
        else:
            # add the character to the dictionary with a count of 1
            hist[char] = 1
    
    # return the histogram
    return hist
