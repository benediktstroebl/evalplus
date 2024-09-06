
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
    # sort the characters
    sorted_chars = sorted(set(test))
    
    # create an empty dictionary to store the count of each character
    char_count = {}
    
    # go through each character and increment the count for that character
    for char in sorted_chars:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count
