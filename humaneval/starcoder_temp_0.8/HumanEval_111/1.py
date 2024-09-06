
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

    if not isinstance(test,str):
        raise TypeError("test should be a string.")
    if test == '':
        return {}
    splitted = test.split(' ')
    letters = []
    for l in splitted:
        if l in letters:
            letters[letters.index(l)] += 1
        else:
            letters.append(l)
    result = {}
    max_count = 0
    for i in range(len(letters)):
        if letters[i] > max_count:
            max_count = letters[i]
            result = {}
            result[letters[i]] = 1
        elif letters[i] == max_count:
            result[letters[i]] = 1
    return result
