
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
    # convert the input to a set to remove duplicates
    test = set(test.lower())
    # keep track of the letter and its count
    letter_count = {}
    # iterate over the set
    for char in test:
        # if the letter is already in the letter_count, increment its count
        if char in letter_count:
            letter_count[char] += 1
        # if the letter is not in the letter_count, add it with a count of 1
        else:
            letter_count[char] = 1
    return letter_count
