
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
    # Remove all spaces
    test = test.replace(" ", "")
    # Convert all characters to lowercase
    test = test.lower()
    # Initialize empty dictionary
    hist = {}
    # Loop through all characters
    for char in test:
        # If character is already in the dictionary, increment count
        if char in hist:
            hist[char] += 1
        # Otherwise, add character to dictionary with a count of 1
        else:
            hist[char] = 1
    return hist
