
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
    # convert the input string to a list of characters
    char_list = list(set(test))

    # count the frequency of each character
    char_count = {}
    for char in char_list:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # return the most frequent character and its count
    return char_count.most_common(1)
