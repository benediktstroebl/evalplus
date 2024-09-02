
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
    t = test.split(' ')
    d = {}
    for i in t:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    largest = max(d.values())
    ret = {}
    for key, value in d.items():
        if value == largest:
            ret[key] = value
    return ret

