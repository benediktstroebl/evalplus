
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
    dictionary = {}
    list_test = test.split()
    for key in list_test:
        if key not in dictionary:
            dictionary[key] = 0
        dictionary[key] += 1
    max_value = max(dictionary.values())
    new_dict = {}
    for key, value in dictionary.items():
        if value == max_value:
            new_dict[key] = value
    return new_dict

