
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
    count = {}
    for i in test.split():
        count[i] = count.get(i, 0) + 1

    max_value = max(count.values())
    max_keys = [k for k, v in count.items() if v == max_value]
    return dict([(k, count[k]) for k in max_keys])

