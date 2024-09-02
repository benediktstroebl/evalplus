
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

    # Write your code below
    hashTable = {}
    newString = test.lower()
    listOfStr = newString.split()
    for char in listOfStr:
        if char in hashTable:
            hashTable[char] += 1
        else:
            hashTable[char] = 1
    newList = []
    for key in hashTable.keys():
        if hashTable[key] == max(hashTable.values()):
            newList.append(key)
    return newList

