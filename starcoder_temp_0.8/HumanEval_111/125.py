
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
    hist = {}
    maxcount = 0
    for c in test.split():
        if c not in hist:
            hist[c] = 0
        hist[c] += 1
        if hist[c] > maxcount:
            maxcount = hist[c]
    for k in hist.keys():
        if hist[k]!= maxcount:
            hist.pop(k)
    return hist

