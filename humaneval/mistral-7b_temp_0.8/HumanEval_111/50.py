
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
    # Your code here
    # Initialize an empty dictionary
    my_dict = {}

    # Iterate over the string, adding each letter and its frequency to the dictionary
    for letter in test:
        if letter in my_dict:
            my_dict[letter] += 1
        else:
            my_dict[letter] = 1

    # Return the dictionary
    return my_dict
