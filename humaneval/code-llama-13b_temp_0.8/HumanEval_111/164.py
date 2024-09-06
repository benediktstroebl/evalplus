
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
    dic = {}
    for x in test:
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
    final = {}
    for x in dic:
        if dic[x] == max(dic.values()):
            final[x] = dic[x]
    return final
