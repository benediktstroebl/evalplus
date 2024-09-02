
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
    dict = {}
    max_value = 0
    for letter in test:
        dict[letter] = dict.get(letter, 0) + 1
        if dict[letter] > max_value:
            max_value = dict[letter]
    result = {}
    for letter, value in dict.items():
        if value == max_value:
            result[letter] = value
    return result
