
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
    dict1 = {}
    for i in test:
        dict1[i] = test.count(i)
    dict2 = {}
    for key, value in dict1.items():
        dict2[value] = key
    dict3 = {}
    for key, value in dict2.items():
        if key not in dict3:
            dict3[key] = []
        dict3[key].append(value)
    return dict3
        
