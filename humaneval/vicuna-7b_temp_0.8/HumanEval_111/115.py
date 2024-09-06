
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
    # convert the input to a list of integers
    test = test.split()
    # initialize the dictionary with the most common letter as key and count as value
    result = {}
    # iterate over the test
    for item in test:
        # if the item is not in the dictionary
        if item in result:
            # increment the count
            result[item] += 1
        else:
            # if the item is not in the dictionary
            result[item] = 1
    return result