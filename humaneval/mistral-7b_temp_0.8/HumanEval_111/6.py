
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
    letter_dict = {}
    for letter in test:
        if letter in letter_dict.keys():
            letter_dict[letter] = letter_dict[letter] + 1
        else:
            letter_dict[letter] = 1
    max_letter = max(letter_dict.items(), key=lambda x: x[1])[0]
    return(max_letter)


