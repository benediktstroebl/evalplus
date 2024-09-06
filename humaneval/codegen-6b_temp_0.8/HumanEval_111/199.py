
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
    from collections import defaultdict

    freq = defaultdict(int)
    for ch in test:
        freq[ch] += 1

    res = {}
    for ch, count in freq.items():
        if count == 1:
            res[ch] = count
        else:
            res[ch] = count,
    return res


