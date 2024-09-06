
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
    # convert the input string to a set of distinct characters
    char_set = set(test.split())
    # initialize a dictionary to store the character and count
    char_count = {}
    # iterate through the character set and count the occurrence of each character
    for char in char_set:
        char_count[char] = char_count.get(char, 0) + 1
    return char_count