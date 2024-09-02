
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
    # replace ' ' with '0'
    test = test.translate(str.maketrans("", "", "0"))
    # split the string
    chunks = test.split()
    # add up the frequency of each letter
    counts = {}
    for i in range(len(chunks)):
        counts[chunks[i]] = counts.get(chunks[i], 0) + 1
    return counts
