
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
    # create a dictionary to store the counts of each letter
    letter_count = {}
    
    # iterate through the string and count the frequency of each letter
    for char in test:
        if char.lower() in letter_count:
            letter_count[char.lower()] += 1
        else:
            letter_count[char.lower()] = 1
    
    # return the dictionary of the letter with the most repetition and containing the corresponding count
    return letter_count.most_common(1)
