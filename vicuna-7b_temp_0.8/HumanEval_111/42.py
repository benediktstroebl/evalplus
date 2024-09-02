
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
    words = test.split()
    max_count = 0
    max_letter = ''
    for word in words:
        counts = Counter(word)
        max_count = max(max_count, counts['a'] + counts['b'] + counts['c'])
        max_letter = max(max_letter, counts['a'] + counts['b'] + counts['c'])
    return {max_letter: max_count}
