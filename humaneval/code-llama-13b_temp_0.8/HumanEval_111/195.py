
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
    letter_dict = dict()
    for letter in test.split():
        if letter_dict.get(letter):
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return {letter: letter_dict[letter] for letter in letter_dict if letter_dict[letter] == max(letter_dict.values())}
