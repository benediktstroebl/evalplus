
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
    # create empty dictionary to store counts
    counts = {}
    
    # iterate through each character in the test string
    for char in test:
        # if the character is in the dictionary, increment the count
        if char in counts:
            counts[char] += 1
        else:
            # if the character is not in the dictionary, add it with a count of 1
            counts[char] = 1
    
    # return the dictionary of counts
    return counts
