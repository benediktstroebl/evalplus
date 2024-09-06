
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
    # Split the string into a list of characters
    chars = test.split()
    # Initialize an empty dictionary to store the frequency of each letter
    char_freq = {}
    # Iterate through the list of characters
    for char in chars:
        # If the character is not in the dictionary, add it with a frequency of 1
        if char not in char_freq:
            char_freq[char] = 1
        # If the character is in the dictionary, update its frequency
        elif char in char_freq:
            char_freq[char] += 1
    # Return the dictionary of frequencies
    return char_freq
