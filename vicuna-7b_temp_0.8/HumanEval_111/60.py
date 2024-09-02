
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
    # convert string to a list of lowercase letters
    letter_list = list(map(lambda x: x.lower(), test.split()))
    
    # sort the list of letters by occurrence
    letter_counts = {}
    for i, letter in enumerate(letter_list):
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

        # if the count is not zero, increment the count for the key
    if len(letter_counts) > 0:
        for key, value in letter_counts.items():
            letter_counts[key] = value

    # return the dictionary of letter and count
    return letter_counts
