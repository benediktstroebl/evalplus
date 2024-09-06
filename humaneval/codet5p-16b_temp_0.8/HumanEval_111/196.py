
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

    
    if test == '':
        return {}

    test = test.split()
    test = list(set(test)) # Remove duplicates

    dict_of_histogram = {}

    for i in range(len(test)):
        dict_of_histogram[test[i]] = test.count(test[i])

    return dict_of_histogram
