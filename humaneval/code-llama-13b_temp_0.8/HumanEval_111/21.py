
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
        dictionary = dict()
        lista = test.split(' ')
        for i in lista:
            if i not in dictionary:
                dictionary[i] = 1
            else:
                dictionary[i] += 1
    
    dictionary_max = dict()
    max_values = list(dictionary.values())
    for key, value in dictionary.items():
        if value == max(max_values):
            dictionary_max[key] = value
    return dictionary_max
