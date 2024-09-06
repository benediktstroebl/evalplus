
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

    test = test.lower() #first convert it into lower case
    test = test.split() #split it into a list
    test = [i for i in test if i!= ''] #remove the empty space from the list
    hist = {}
    for i in test:
        if i not in hist:
            hist[i] = test.count(i)
    max_key = ''
    max_val = 0
    for key, value in hist.items():
        if value > max_val:
            max_key = key
            max_val = value
        else:
            pass
    return hist








