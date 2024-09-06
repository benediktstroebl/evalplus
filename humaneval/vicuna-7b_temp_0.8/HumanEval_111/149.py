
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
    # Convert input string to a set of characters
    input_set = set(test)
    # Create an empty dictionary to store the count of each letter
    letter_count = {}
    # Iterate through the set of characters
    for char in input_set:
        # If the letter is not in the dictionary, add it with a count of 1
        if char not in letter_count:
            letter_count[char] = 1
            # If this is the first time seeing the letter, add it to the dictionary
            if char not in input_set:
                input_set.remove(char)
    # Iterate through the dictionary of characters and count the letters
    for char in input_set:
        letter_count[char] += 1
    # Return the dictionary of letters and their corresponding count
    return letter_count