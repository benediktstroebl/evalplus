
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

    # YOUR CODE HERE
    # Create an empty dictionary
    output = {}
    # Split the input string into a list of strings
    string_list = test.split()
    # Sort the list so that the most repeated letter is first
    string_list.sort(key=lambda x: x[0])
    # For each letter in the list
    for char in string_list:
        # If it is already in the dictionary, add one to the count
        if char in output:
            output[char] += 1
        # Otherwise, initialize the count
        else:
            output[char] = 1
    return output

