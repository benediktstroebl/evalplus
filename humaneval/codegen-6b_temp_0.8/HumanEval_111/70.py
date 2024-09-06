
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
    word_counts = {}
    for char in test:
        if char in word_counts:
            word_counts[char] += 1
        else:
            word_counts[char] = 1
    
    result = {}
    for key, value in word_counts.items():
        if value > result.get(value, 0):
            result[value] = key
    
    return result
