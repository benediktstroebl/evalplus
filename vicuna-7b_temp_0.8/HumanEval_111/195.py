
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
    # Check if the input is empty
    if not test:
        return {}
    
    # Split the input into a list of characters
    chars = test.split()
    
    # Initialize an empty dictionary to store the histogram
    hist = {}
    
    # Loop through the characters and increment the count for each letter
    for char in chars:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    
    # Return the histogram
    return hist
