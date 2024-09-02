
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
    # getting the string into a list
    test_list = test.split(" ")
    # creating an empty dictionary
    dict_of_letters = {}
    # iterate over the list
    for letter in test_list:
        # if the letter is already in the dictionary
        if letter in dict_of_letters:
            # update the value of the letter
            dict_of_letters[letter] += 1
        else:
            # add the letter to the dictionary
            dict_of_letters[letter] = 1
    return dict_of_letters

