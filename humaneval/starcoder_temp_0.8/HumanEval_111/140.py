
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
    res = {}
    res[test[0]] = 1
    for i in range(1, len(test)):
        if test[i] in res:
            res[test[i]] += 1
        else:
            res[test[i]] = 1
    
    max_count = max(res.values())
    return [i for i in res if res[i] == max_count]

