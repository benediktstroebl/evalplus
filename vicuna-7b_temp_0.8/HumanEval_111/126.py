
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
    # convert input string to a set of unique characters
    unique_chars = set(test)
    
    # initialize result dict
    result = {}
    
    # iterate through unique characters
    for char in unique_chars:
        # increment count for current character
        result[char] = result.get(char, 0) + 1
    
    # return result dict
    return result
