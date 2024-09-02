
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

    if not test:
        return {}

    test_dict = {}
    for c in test:
        test_dict.setdefault(c, 0)
        test_dict[c] += 1

    max_value = max(test_dict.values())
    return {k: v for k, v in test_dict.items() if v == max_value}

