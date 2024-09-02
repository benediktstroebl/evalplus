
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
    # create dictionary of letters with the same occurrence
    d = {}
    # create dictionary of letters with the most occurrence
    max_letter = {}
    # split string into list of letters
    test = test.split(" ")
    # iterates through the string of letters and adds them to the dictionary
    for i in test:
        d[i] = d.get(i, 0) + 1
    # finds the most occurrence of letters in the dictionary
    for i in d:
        if d[i] > max_letter.get(i, 0):
            max_letter[i] = d[i]
    return max_letter
