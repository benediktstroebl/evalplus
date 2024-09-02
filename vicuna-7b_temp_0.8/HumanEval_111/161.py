
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
    # convert the input string to a set of unique characters
    unique = set(test)
    
    # initialize the dictionary with the most common character as the key and 0 as the value
    histogram = {unique[0]: 1}
    
    # iterate through the remaining characters, incrementing the count for each repeat
    for char in unique:
        histogram[char] += 1
    
    return histogram
