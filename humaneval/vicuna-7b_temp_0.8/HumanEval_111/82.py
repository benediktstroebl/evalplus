
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
    # Create a set to store the seen letters
    seen = set()
    
    # Create a dictionary to store the count of each letter
    counts = {}
    
    # Iterate through the input string
    for char in test:
        # If the char is in the seen set, increment the count
        if char in seen:
            counts[char] += 1
        else:
            # Add the char to the seen set and increment the count
            seen.add(char)
            counts[char] = 1
    
    # Return the dictionary of counts
    return counts
