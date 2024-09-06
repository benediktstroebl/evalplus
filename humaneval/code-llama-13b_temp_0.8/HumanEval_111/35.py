
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
    words = test.split()
    dic = {}
    for i in words:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    result = {}
    for i, j in dic.items():
        if j in result:
            result[j].append(i)
        else:
            result[j] = [i]
    return result

