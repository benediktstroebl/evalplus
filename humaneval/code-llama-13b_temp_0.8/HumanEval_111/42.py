
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
    if not test:
        return {}

    hash_table = dict()
    for char in test.split():
        hash_table[char] = hash_table.get(char, 0) + 1

    max_repetition = max(hash_table.values())
    return dict(filter(lambda x: x[1] == max_repetition, hash_table.items()))
