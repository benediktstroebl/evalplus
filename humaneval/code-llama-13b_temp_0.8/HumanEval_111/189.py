
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
    myDict = {}
    for i in test.split(' '):
        if i in myDict:
            myDict[i] += 1
        else:
            myDict[i] = 1

    max = 0
    for i in myDict:
        if myDict[i] >= max:
            max = myDict[i]
    
    newDict = {}
    for i in myDict:
        if myDict[i] == max:
            newDict[i] = myDict[i]
    
    return newDict
