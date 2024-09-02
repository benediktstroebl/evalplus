
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
    dict_letters = {}
    max_occur = 0
    for letter in test.split():
        dict_letters[letter] = dict_letters.get(letter, 0) + 1
        max_occur = max(dict_letters[letter], max_occur)
    res_dict = {}
    for key in dict_letters.keys():
        if dict_letters[key] == max_occur:
            res_dict[key] = dict_letters[key]
    return res_dict
