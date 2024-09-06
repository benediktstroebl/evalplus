
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
    # Convert the input string to a list of characters
    chars = set(test.split())
    
    # Create an empty dictionary to store the counts
    counts = {}
    
    # Loop over the characters in the input string
    for char in chars:
        # If the count is not in the dictionary, increment it
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    
    # Return the dictionary of counts
    return counts
