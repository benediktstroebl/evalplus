
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
    dict = {}
    for i in test.split(' '):
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
        max = 0
        key = ''
        for k,v in dict.items():
            if v > max:
                max = v
                key = k
    return {key:max}

