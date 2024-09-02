
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
    
    if test == "":
        return {}
    dict = {}
    for i in test.split(" "):
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    maxi = max(dict.values())
    result = {}
    for i in dict:
        if dict[i] == maxi:
            result[i] = dict[i]
    return result
    
    
