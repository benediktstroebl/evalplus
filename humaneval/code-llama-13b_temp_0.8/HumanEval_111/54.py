
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
    testDict = {}
    letters = test.split()
    for letter in letters:
        if letter in testDict:
            testDict[letter] += 1
        else:
            testDict[letter] = 1
    returnDict = {}
    for key, value in testDict.items():
        if value in returnDict:
            returnDict[value].append(key)
        else:
            returnDict[value] = [key]
    return returnDict
