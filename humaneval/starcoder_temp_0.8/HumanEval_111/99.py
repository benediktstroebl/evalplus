
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

    # initialize dictionary to hold values of letter and its count
    histogram = {}

    # if the input string is empty, return an empty dictionary
    if test == '':
        return histogram

    # split the input string and count each letter
    split_test = test.split(' ')
    letter_count = Counter(split_test)

    # find the most frequent letter
    most_common_letter = letter_count.most_common(1)

    # create a dictionary containing the most frequent letter and its count
    histogram[most_common_letter[0][0]] = most_common_letter[0][1]

    # return dictionary with the most frequent letter
    return histogram

