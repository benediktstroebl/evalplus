
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
    hist = {}
    for char in test:
        if char not in hist:
            hist[char] = 0
        hist[char] += 1
    most = ''
    most_count = 0
    for char, count in hist.items():
        if count > most_count:
            most = char
            most_count = count
        elif count == most_count:
            most += ' / ' + char
    return {most: most_count}

