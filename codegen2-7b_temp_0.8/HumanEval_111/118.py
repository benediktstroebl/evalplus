
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
    letters_dict = {}
    for letter in test:
        if letter not in letters_dict:
            letters_dict[letter] = 1
        else:
            letters_dict[letter] += 1
    sorted_letters = sorted(letters_dict.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_letters

