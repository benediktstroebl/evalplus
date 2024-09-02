
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
    if len(test) == 0:
        return {}
    maxi = 0
    dicti = {}
    for i in test.split():
        if i in dicti:
            dicti[i] += 1
        else:
            dicti[i] = 1
        if maxi < dicti[i]:
            maxi = dicti[i]
    newdict = {}
    for i in dicti:
        if maxi == dicti[i]:
            newdict[i] = maxi
    return newdict
