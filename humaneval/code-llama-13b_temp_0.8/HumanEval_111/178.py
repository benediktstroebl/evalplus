
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

    letters = test.split()
    dict_letters = {}

    for letter in letters:
        if letter not in dict_letters:
            dict_letters[letter] = 1
        else:
            dict_letters[letter] += 1

    max_letter = max(dict_letters.values())
    letters_max = []

    for letter in dict_letters.keys():
        if dict_letters[letter] == max_letter:
            letters_max.append(letter)

    dict_max_letters = {}
    for letter in letters_max:
        dict_max_letters[letter] = max_letter

    return dict_max_letters

