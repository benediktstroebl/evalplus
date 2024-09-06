
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
    keys = set()
    count = {}
    for letter in test:
        if letter.lower() not in count:
            keys.add(letter.lower())
            count[letter.lower()] = 1
    keys_list = sorted(list(keys))
    return dict(zip(keys_list, [count[key] for key in keys_list]))