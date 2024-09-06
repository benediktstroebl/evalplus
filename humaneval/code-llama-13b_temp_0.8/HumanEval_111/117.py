
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
        return dict()
    else:
        lst = test.split(' ')
        dic = {}
        for i in lst:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        max_ = max(dic.values())
        return {k:v for k, v in dic.items() if v == max_}
