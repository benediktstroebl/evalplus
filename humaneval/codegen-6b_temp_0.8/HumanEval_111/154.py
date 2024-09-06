
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
    # get list of letters in string
    letters = test.lower().split(' ')
    # make new dictionary to store counts
    char_dict = {}
    # initialize new dictionary
    for char in letters:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    # return dictionary
    return char_dict

assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
assert histogram('a b b a') == {'a': 2, 'b': 2}
assert histogram('a b c a b') == {'a': 2, 'b': 2}
assert histogram('b b b b a') == {'b': 4}
assert histogram('') == {}
assert histogram('a b c A a') == {'a': 2, 'b': 2, 'c': 1}
