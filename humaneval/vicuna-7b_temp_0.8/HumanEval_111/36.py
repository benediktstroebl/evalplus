
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
    # initialize a dictionary with the count of each letter as the value and the letter as the key
    letter_count = {}
    
    # iterate through the string
    for letter in test:
        # if the letter is in the dictionary
        if letter in letter_count:
            # increment the count for the letter
            letter_count[letter] += 1
        else:
            # if the letter is not in the dictionary, add it with a count of 1
            letter_count[letter] = 1
    
    # return the dictionary of letters and their counts
    return letter_count
