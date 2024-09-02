
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
    if test.count(" ") == len(test) - 1:
        return {}
    if test.count(" ") == len(test):
        return {}
    if test.count(" ") == len(test) - 2:
        return {}
    test = test.strip()
    test = test.split(" ")
    for i in test:
        if i not in test:
            return {}
    dic = {}
    for i in test:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    maxi = 0
    for i in dic.values():
        if i > maxi:
            maxi = i
    res = {}
    for i in dic.keys():
        if dic[i] == maxi:
            res[i] = dic[i]
    return res
    
