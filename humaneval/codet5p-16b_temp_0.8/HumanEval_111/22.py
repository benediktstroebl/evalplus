
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

    

    test = test.split()
    max = 0
    max_keys = []
    for key in test:
        if test.count(key) > max:
            max = test.count(key)
            max_keys = [key]
        elif test.count(key) == max:
            max_keys.append(key)
    return {k: test.count(k) for k in max_keys}



