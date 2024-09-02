
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
    test = test.lower()
    counts = {}
    for letter in test:
        if letter not in counts:
            counts[letter] = 0
        counts[letter] += 1
    
    if len(test) == 0:
        return counts
    else:
        return max(counts.items(), key=operator.itemgetter(1))[0]

    
