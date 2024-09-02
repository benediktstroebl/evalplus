
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
    histo = {}
    for c in test:
        if 'a' <= c <= 'z':
            if c in histo:
                histo[c] += 1
            else:
                histo[c] = 1
    
    # Note: order is irrelevant, so put it back in the list:
    output = [k for k in histo.iterkeys()]
    output.sort()
    
    return dict(zip(output, [histo[k] for k in output]))
