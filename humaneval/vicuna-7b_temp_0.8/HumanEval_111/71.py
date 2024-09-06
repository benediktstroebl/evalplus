
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
    letters = set(test.lower())
    max_count = 0
    max_letter = ''
    for letter in letters:
        if letter in letters:
            count = letters.count(letter)
            if count > max_count:
                max_count = count
                max_letter = letter
    if max_count == 0:
        return {}
    else:
        return {'max': max_letter, 'count': max_count}
