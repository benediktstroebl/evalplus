
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

    
    if len(test) == 0:
        return {}

    test = test.split()
    histogram = {}
    most_repetition = []

    for element in test:
        if element not in histogram:
            histogram[element] = 1
        else:
            histogram[element] += 1

    return histogram

    

