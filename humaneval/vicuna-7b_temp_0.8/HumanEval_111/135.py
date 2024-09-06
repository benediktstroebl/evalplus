
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
    # convert string to set of characters
    char_set = set(test.lower())
    
    # create an empty dictionary to store the frequency of each character
    freq = {}
    
    # iterate through each character in the set
    for char in char_set:
        # increment the count for the current character
        freq[char] = freq.get(char, 0) + 1
        
    # return the dictionary of most frequent characters
    return freq
