
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
    # convert input to a list of characters
    input_list = [char.lower() for char in test.split()]
    # count the frequency of each character
    letter_count = {}
    for char in input_list:
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    # return the most frequent letter and its count
    return max(letter_count.items(), key=letter_count.get)
