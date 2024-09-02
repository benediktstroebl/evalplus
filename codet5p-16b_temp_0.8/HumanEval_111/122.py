
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

    d = {}
    max_value = 0
    for ch in test:
        if ch not in d:
            d[ch] = 1
        else:
            d[ch] += 1
            if d[ch] > max_value:
                max_value = d[ch]
    return {key: d[key] for key in d if d[key] == max_value}
