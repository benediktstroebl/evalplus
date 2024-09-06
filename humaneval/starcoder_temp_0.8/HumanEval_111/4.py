
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
    letters_occurrences = {}
    for letter in letters:
        letters_occurrences[letter] = letters_occurrences.get(letter, 0) + 1
    max_occurrence = max(letters_occurrences.values())
    return {k: v for k, v in letters_occurrences.items() if v == max_occurrence}
