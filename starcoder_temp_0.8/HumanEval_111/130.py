
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

    # Initialize histogram dictionary
    histogram = {}

    # Split input string in space separated lowercase letters
    input_list = test.split()

    # Compute histogram
    for letter in input_list:
        histogram[letter] = histogram.get(letter, 0) + 1

    # Return histogram dictionary
    return histogram
