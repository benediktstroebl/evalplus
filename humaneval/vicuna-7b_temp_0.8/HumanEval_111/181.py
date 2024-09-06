
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
    # convert string to a list of characters
    char_list = list(test)
    # sort the list by frequency
    char_list = sorted(char_list, key=lambda x: char_list.count(x), reverse=True)
    # group the characters by frequency and return the results
    return dict(enumerate(char_list))
