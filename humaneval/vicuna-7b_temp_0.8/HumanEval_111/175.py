
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
    # Create a dictionary to store the counts
    counts = {}
    
    # Iterate through the characters in the test string
    for c in test:
        # If the character is in the counts dictionary, increment the count
        if c in counts:
            counts[c] += 1
        else:
            # If the character is not in the counts dictionary, add it with a count of 1
            counts[c] = 1
    
    # Return the dictionary of counts
    return counts
