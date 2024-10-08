
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
    words = test.split()
    hist = {}
    for word in words:
        if word in hist:
            hist[word] += 1
        else:
            hist[word] = 1
    max_val = max(hist.values())
    max_key = max(hist.keys(), key=hist.get)
    return max_key, max_val
