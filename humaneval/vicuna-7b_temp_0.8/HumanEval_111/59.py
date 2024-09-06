
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
    # convert the input string to a set of unique characters
    unique_chars = set(test)
    # sort the set
    unique_chars.sort()
    # create a dictionary with the most frequent letter and its count
    hist = {}
    for char in unique_chars:
        hist[char] = 1
    # add the remaining characters with their count
    for char in unique_chars:
        hist[char] += 1
    return hist
