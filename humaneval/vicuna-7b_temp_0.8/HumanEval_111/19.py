
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
    # remove all whitespaces
    test = test.lower().split(' ')
    # convert to set to get rid of duplicates
    test = set(test)
    # count the frequency of each letter
    count = {}
    for letter in test:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    result = {}
    for key, value in count.items():
        if value == 1 or value == 2:
            result[key] = value
    return result