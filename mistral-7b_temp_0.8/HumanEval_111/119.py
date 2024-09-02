
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
    # Initializing dictionary and creating for loop
    dictionary = {}
    for letter in test.split():
        # Checking if the letter is already in the dictionary
        if letter in dictionary.keys():
            # If yes, increasing the counter by 1
            dictionary[letter] += 1
        # If the letter is not in the dictionary, adding it with counter 1
        else:
            dictionary[letter] = 1
    # Returning the dictionary
    return dictionary
