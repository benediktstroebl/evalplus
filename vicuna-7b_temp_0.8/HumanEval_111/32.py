
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
    n = 0
    result = {}
    for c in test:
        n += 1
        if n > len(test):
            break
    result[test[n-1]] = 1
    for i in range(n-1, -1, -1):
        if test[i] in result:
            result[test[i]] += 1
    return result
