
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
    # Make a list of the char from the string
    char = list(test)
    # Make a dictionary of the char in the list
    char_dict = {}
    # Iterate over the char in the list and count the number of times the char appears
    for x in char:
        if x not in char_dict:
            char_dict[x] = 1
        else:
            char_dict[x] += 1
    # Sort the dictionary by the value in descending order
    return sorted(char_dict, key=char_dict.get, reverse=True)


