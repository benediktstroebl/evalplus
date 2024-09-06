
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
    s = test.split()
    for x in s:
        if x not in histo:
            histo[x] = 1
        else:
            histo[x] += 1
    max_value = 0
    for x, count in histo.items():
        if count > max_value:
            max_value = count
            max_keys = [x]
        elif count == max_value:
            max_keys.append(x)
    if len(max_keys) == 1:
        return {max_keys[0]: max_value}
    return {key: max_value for key in max_keys}

