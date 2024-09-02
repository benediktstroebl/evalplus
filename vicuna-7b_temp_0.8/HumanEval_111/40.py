
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
    # convert the string to lowercase
    test = test.lower()
    # split the string into a list of characters
    words = test.split()
    # initialize a dictionary to store the count of each letter
    counts = {}
    # iterate over the list of characters
    for char in words:
        # if the character is in the dictionary, increment its count
        if char in counts:
            counts[char] += 1
        # if the character is not in the dictionary, add it with a count of 1
        else:
            counts[char] = 1
    # return the dictionary of counts
    return counts
