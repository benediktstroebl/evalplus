
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
    test_list = test.split()
    result = {}
    for i in test_list:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    max_val = 0
    max_key = []
    for i, j in result.items():
        if j > max_val:
            max_val = j
            max_key = [i]
        elif j == max_val:
            max_key.append(i)
    return {i:j for i, j in result.items() if j == max_val}
