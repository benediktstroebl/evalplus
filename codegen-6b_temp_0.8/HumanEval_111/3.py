
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
    # Get each letter from the string passed in
    letters = test.split(" ")
    # Cast each letter to lowercase, so we can do a comparison
    letters = [letter.lower() for letter in letters]
    # Initialize an empty dictionary
    histograms = {}
    # For each letter in the string, if the letter was already in the dictionary, increment the value of that key by 1
    for letter in letters:
        if letter in histograms:
            histograms[letter] += 1
        else:
            histograms[letter] = 1
    return histograms

