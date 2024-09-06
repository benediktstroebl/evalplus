
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
    # return dict([(char, test.count(char)) for char in test])
    # return dict([(char, test.count(char)) for char in list(set(test))])
    # return dict([(char, test.count(char)) for char in test if char not in dict.keys()])

    return dict(zip(set(test), [test.count(letter) for letter in set(test)]))

