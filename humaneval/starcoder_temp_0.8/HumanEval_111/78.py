
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

    for l in test.split(' '):
        if l in histo:
            histo[l] += 1
        else:
            histo[l] = 1

    max_val = 0
    max_key = ""

    for key, val in histo.items():
        if val > max_val:
            max_val = val
            max_key = key

    result = {max_key: max_val}

    for key, val in histo.items():
        if val == max_val and key!= max_key:
            result[key] = val

    return result
