
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
    for i in test.split():
        hist[i] = hist.get(i, 0) + 1
    res = max(hist, key=hist.get)
    print(res, hist[res])
    if list(hist.values()).count(hist[res]) == 1:
        return hist
    else:
        return {k:v for k, v in hist.items() if v == hist[res]}

