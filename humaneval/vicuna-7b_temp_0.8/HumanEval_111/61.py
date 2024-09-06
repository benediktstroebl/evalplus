
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
    char_list = test.split()
    # initialize an empty dictionary to store the letter and its count
    char_dict = {}
    # iterate through each character in the list
    for char in char_list:
        # if the character is in the dictionary, increment its count
        if char in char_dict:
            char_dict[char] += 1
        # if the character is not in the dictionary, add it with a count of 1
        else:
            char_dict[char] = 1
    # return the dictionary of letters and their counts
    return char_dict
