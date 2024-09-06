
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
    letter_count = {}
    for letter in test.split():
        letter_count[letter] = letter_count.get(letter, 0) + 1
    
    if not letter_count:
        return {}

    max_count = max(letter_count.values())
    letter_count = {letter: count/max_count for letter, count in letter_count.items() if count/max_count >= 0.5}
    return letter_
