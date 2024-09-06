
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
    # remove any whitespace and convert to lowercase
    test = test.strip().lower()
    # split the input into a list of characters
    chars = test.split()
    # create an empty dictionary to store the counts
    counts = {}
    # loop through the list of characters and increment the count for each letter
    for char in chars:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    # return the dictionary of counts
    return counts
