
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
    # your code here
    # the basic idea is to count the letter for the first time, then count the letter again
    # to compare with the previous one.
    if test == '':
        return {}
    if len(test) == 1:
        return {test: 1}
    result = {}
    key = test[0]
    key_num = 1
    for i in range(len(test)-1):
        if test[i] == key:
            key_num += 1
        else:
            if key in result:
                result[key] += key_num
                key = test[i]
                key_num = 1
            else:
                result[key] = key_num
                key = test[i]
                key_num = 1
    if key in result:
        result[key] += key_num
    else:
        result[key] = key_num

    return result
