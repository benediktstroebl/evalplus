
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
    # Check if the string is empty
    if not test:
        return {}

    # Split the string into a list of characters
    words = test.split()

    # Initialize a dictionary to store the counts of each character
    counts = {}

    # Loop through the list of characters
    for char in words:
        # If the character is already in the dictionary, increment its count
        if char in counts:
            counts[char] += 1
        else:
            # If the character is not already in the dictionary, add it with a count of 1
            counts[char] = 1

    # Return the dictionary of characters and their counts
    return counts
