
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
    if test == '':
        return {}
    else:
        d = {}
        for c in test:
            if c not in d:
                d[c] = 1
            else:
                d[c] = d[c] + 1
        m = 0
        result = []
        for key,value in d.items():
            if value >= m:
                if value > m:
                    result = []
                result.append(key)
                m = value
        return {key:value for key,value in d.items() if key in result}
