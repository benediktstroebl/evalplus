
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

    d = {}
    for elem in test.split():
        if elem not in d.keys():
            d[elem] = 1
        else:
            d[elem] += 1
    max_repetition = max(d.values())
    ret = {}
    for key, value in d.items():
        if value == max_repetition:
            ret[key] = value
    return ret
