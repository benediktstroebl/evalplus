
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
    # initialize a dictionary to store the histogram
    hist = {}
    
    # loop through the input string
    for char in test:
        # if the character is not a letter
        if not char.isalpha():
            continue
        
        # if the character is not already in the dictionary
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
    
    return hist
