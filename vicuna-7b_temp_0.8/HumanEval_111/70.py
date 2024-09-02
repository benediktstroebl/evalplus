
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
    # split the string into a list of characters
    char_list = list(test)
    # sort the list by frequency
    char_list = sorted(char_list, key=lambda x: len(filter(str.islower, x)))
    # store the most common character in a dictionary
    hist = {}
    for char in char_list:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    return hist
