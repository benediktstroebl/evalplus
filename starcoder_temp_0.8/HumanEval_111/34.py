
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
    test1 = test.split(" ")
    test2 = {}
    for i in test1:
        if i not in test2:
            test2[i] = 1
        else:
            test2[i] += 1
    max_key = max(test2, key=lambda k: test2[k])
    if test2[max_key] > 1:
        return {max_key: test2[max_key]}
    else:
        return {k: v for k, v in test2.items() if v == test2[max_key]}

