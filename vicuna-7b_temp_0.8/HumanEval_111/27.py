
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
    # convert to lowercase
    test_lowercase = test.lower()
    # split the string into a list of characters
    words = test_lowercase.split()
    # initialize the dictionary
    count = {}
    # iterate through the list of characters
    for char in words:
        # if the character is in the dictionary and the count is higher than the previous highest count
        if char in count and count[char] > count.get(char, 0):
            count[char] += 1
        else:
            count[char] = 1
    return count
