
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
    max_value = 0
    max_letter = ''
    res = {}
    for letter in test:
        if letter not in res:
            res[letter] = 0
        res[letter] += 1
        if max_value < res[letter]:
            max_value = res[letter]
            max_letter = letter
    return res

assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
assert histogram('a b b a') == {'a': 2, 'b': 2}
assert histogram('a b c a b') == {'a': 2, 'b': 2}
assert histogram('b b b b a') == {'b': 4}
assert histogram('') == {}
assert histogram('a a a') == {'a': 3}
assert histogram('a a a a') == {'a': 4}
assert histogram('b') == {'b': 1}
assert histogram('b b') == {'b': 2}
assert histogram('b b b') == {'b': 3}
assert histogram('a a a a') == {'a': 5}