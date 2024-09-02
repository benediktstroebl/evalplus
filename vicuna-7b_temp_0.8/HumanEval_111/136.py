
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
    # Create a dictionary to hold the counts
    counts = {}
    
    # Loop through each character in the input string
    for char in test:
        # If the character is in the dictionary, increment its count
        if char in counts:
            counts[char] += 1
        else:
            # If this is the first time seeing this character, add it to the dictionary with a count of 1
            counts[char] = 1
    
    # Return the dictionary of counts
    return counts
