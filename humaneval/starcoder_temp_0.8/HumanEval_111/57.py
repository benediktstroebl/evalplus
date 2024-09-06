
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
    # List of letters in the string
    letters = test.split()
    # Empty dictionary to hold the letters and their count
    h = {}
    # Iterate over letters and add 1 to the count of each letter
    for i in letters:
        h[i] = h.get(i, 0) + 1
    # Return the key with the most count
    return max(h, key=h.get)
