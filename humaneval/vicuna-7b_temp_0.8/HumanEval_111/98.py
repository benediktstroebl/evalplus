
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
    # split the input string into a list of characters
    words = test.split()
    # initialize a dictionary to store the count of each letter
    letter_count = {}
    # iterate through the list of characters
    for char in words:
        # if the char is in the dictionary, increment the count
        if char in letter_count:
            letter_count[char] += 1
        else:
            # if the char is not in the dictionary, add it with a count of 1
            letter_count[char] = 1
    # return the dictionary of the letter with the most repetition and containing the corresponding count
    return letter_count.most_common(1)
