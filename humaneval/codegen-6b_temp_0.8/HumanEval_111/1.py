
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
    # BEGIN solution
    hist = {}
    for char in test:
        if char in hist.keys():
            hist[char] += 1
        else:
            hist[char] = 1
    max_val = 0
    max_key = None
    for key, val in hist.iteritems(): 
        if val > max_val:
            max_val = val
            max_key = key
        elif val == max_val:
            max_val = val
            max_key = key
    return {max_key: max_val}
    # END solution

