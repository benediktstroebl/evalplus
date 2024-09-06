
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
    else:
        test = test.split(' ')
        count = {}
        maxcount = 0
        for i in test:
            if count.get(i) == None:
                count[i] = 1
            else:
                count[i] += 1
            if count[i] > maxcount:
                maxcount = count[i]
        temp = []
        for key,value in count.items():
            if value == maxcount:
                temp.append(key)
        return temp
