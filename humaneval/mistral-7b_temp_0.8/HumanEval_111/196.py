
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
    # create a dictionary to hold the letters and their corresponding counts
    letters_count = {}
    for letter in test:
        # if the letter is not in the dictionary, add it with a count of 1
        if letter not in letters_count:
            letters_count[letter] = 1
        # if the letter is already in the dictionary, increment its count
        else:
            letters_count[letter] += 1

    return letters_count
