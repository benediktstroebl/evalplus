
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
    n = 0
    d = {}
    for i in range(len(test)):
        if test[i] == 'a':
            n += 1
        elif test[i] == 'b':
            if n == 0:
                d['a'] = 1
            n += 1
        elif test[i] == 'c':
            if n == 0:
                d['a'] = 1
            d['b'] = 1
            n += 1
        else:
            if n == 0:
                d[test[i]] = 1
            n += 1
    return d
