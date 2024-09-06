
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
    d = {}
    i = 0
    while i < len(test):
        if test[i] not in d.keys():
            d[test[i]] = 1
            i += 1
        else:
            d[test[i]] += 1
            i += 1
    return d

    # if len(test) == 0:
    #     return {}
    # return {test[0]: 1}
    # elif len(test) == 1:
    #     return {test[0]: 1}
    # else:
    #     d = {test[0]: 1}
    #     i = 1
    #     while i < len(test):
    #         if test[i] not in d.keys():
    #             d[test[i]] = 1
    #             i += 1
    #         else:
    #             d[test[i]] += 1
    #             i += 1
    #     return d

