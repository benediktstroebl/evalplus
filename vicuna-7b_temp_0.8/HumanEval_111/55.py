
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
    # initialize empty dictionary
    d = {}
    
    # for each letter in the string
    for letter in test:
        # if the letter is not in the dictionary yet
        if letter not in d:
            # increment the count
            d[letter] = 1
        # if the letter is in the dictionary and the count is greater than the current count
        elif letter in d and d[letter] > d.get(letter, 0):
            # increment the count
            d[letter] += 1
        # if the letter is in the dictionary and the count is equal to the current count
        elif letter in d and d[letter] == d.get(letter, 0):
            # add the letter to the dictionary
            d[letter] += 1
    
    # return the dictionary
    return d
