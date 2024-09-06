
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
    for letter in test:
        if letter in test_dict:
            test_dict[letter] += 1
        else:
            test_dict[letter] = 1

    test_dict_items = test_dict.items()
    max_count = max(test_dict_items, key=lambda x: x[1])[1]
    return dict(filter(lambda x: x[1] == max_count, test_dict.items()))

