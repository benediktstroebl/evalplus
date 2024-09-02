
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
        result = {}
        data = test.split(' ')
        for word in data:
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1
        max_value = max(result.values())
        return {key: value for key, value in result.items() if value == max_value}

