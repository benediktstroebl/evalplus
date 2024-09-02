
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
    # convert string to a set of unique characters
    unique_chars = set(test.lower())
    # add the number of times each character appears in the string
    counts = {}
    for char in unique_chars:
        counts[char] = test.count(char)
    # remove any keys with count of 0
    counts = dict((k, v) for k, v in counts.items() if v > 0)
    # return the letter and count as a tuple
    return [(k, v) for k, v in counts.items()]
