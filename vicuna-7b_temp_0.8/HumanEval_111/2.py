
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
    # split string into list of individual letters
    letters = test.split()
    # initialize empty dictionary to store letter-count pairs
    freq = {}
    # iterate through each letter
    for letter in letters:
        # if letter is not in dictionary, add it with a count of 1
        if letter not in freq:
            freq[letter] = 1
        # if letter is already in dictionary, increment its count
        else:
            freq[letter] += 1
    # return dictionary of letter-count pairs
    return freq
