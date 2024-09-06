
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
    l = test.split()
    l = sorted(l)
    d = {}
    # print(l)
    for x in l:
        if x not in d:
            d[x] = 1
        else:
            d[x] += 1
    # print(d)
    d_ = {}
    v = max(d.values())
    for k, v in d.items():
        if v == v:
            d_[k] = v
    return d_
