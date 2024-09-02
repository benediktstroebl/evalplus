
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
    for char in test:
        if char in dictionary:
            dictionary[char] += 1
        else:
            dictionary[char] = 1
    if dictionary == {}:
        return dictionary
    elif max(dictionary.values()) == 1:
        for key, value in dictionary.items():
            if value == 1:
                return {key: value}
    else:
        final = {}
        for key, value in dictionary.items():
            if value == max(dictionary.values()):
                final[key] = value
        return final


