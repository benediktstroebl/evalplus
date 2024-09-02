
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
    #Your code here
    d = {}
    for l in test.split():
        if l in d:
            d[l] += 1
        else:
            d[l] = 1

    vals = d.values()
    keys = d.keys()
    max_val = max(vals)
    res = {}
    for i, val in enumerate(vals):
        if val == max_val:
            res[keys[i]] = val
    return res
