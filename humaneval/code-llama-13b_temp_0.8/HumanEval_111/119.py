
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
    d = dict()
    for i in test.split():
        d[i] = test.count(i)
    temp = dict()
    for i in d:
        if d[i] not in temp:
            temp[d[i]] = [i]
        else:
            temp[d[i]].append(i)
    res = dict()
    for i in temp:
        if len(temp[i]) == 1:
            res[temp[i][0]] = i
        else:
            for j in temp[i]:
                res[j] = i
    return res
