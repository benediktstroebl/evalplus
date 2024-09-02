
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
    for letter in test.split(' '):
        if letter in hist:
            hist[letter] += 1
        else:
            hist[letter] = 1
    
    most_frequent = {}
    
    for letter in hist:
        if hist[letter] > most_frequent.get('count', 0):
            most_frequent = {'letter': letter, 'count': hist[letter]}
    
    if len(most_frequent) == 0:
        return most_frequent
    if most_frequent['count'] == 1:
        return most_frequent['letter']
    return most_frequent

