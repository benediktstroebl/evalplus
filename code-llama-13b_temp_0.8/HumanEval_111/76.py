
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
    
    dict_hist = {}
    for letter in test.split(' '):
        dict_hist[letter] = test.count(letter)
    
    max_letter = max(dict_hist, key=dict_hist.get)
    dict_return = {key: value for (key, value) in dict_hist.items() if dict_hist[max_letter] == value}
    return dict_return
