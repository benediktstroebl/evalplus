
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
    # sort the test string
    test = sorted(test)
    # initialize a dictionary to store the counts of each letter
    letter_count = {}
    # iterate through the sorted test string
    for char in test:
        # if the character is not a letter
        if char not in string.ascii_letters:
            continue
        # if the letter has already been counted
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
