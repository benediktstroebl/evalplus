
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
    letters = set(test.split())
    hist = {}
    max_freq = 0
    
    for char in letters:
        if char in hist:
            hist[char] += 1
        else:
            hist[char] = 1
            hist[letters.index(char)] = 1
    
    for char in hist:
        if hist[char] > max_freq:
            max_freq = hist[char]
    
    return max_freq