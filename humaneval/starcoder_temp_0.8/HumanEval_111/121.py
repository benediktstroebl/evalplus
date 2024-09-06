
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
    letters = test.split()
    letter_dict = {}
    for letter in letters:
        letter_dict[letter] = letters.count(letter)
    max_value = max(letter_dict.values())
    max_keys = []
    for key in letter_dict.keys():
        if letter_dict[key] == max_value:
            max_keys.append(key)
    if len(max_keys) == 1:
        return {max_keys[0]: max_value}
    else:
        return {key: letter_dict[key] for key in max_keys}

