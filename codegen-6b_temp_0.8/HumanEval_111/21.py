
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
    
    histo = {}
    letters = test.split()
    
    for l in letters:
        if l in histo:
            histo[l] += 1
        else:
            histo[l] = 1
    
    max_letters = None
    max_count = 0
    for key in histo:
        if histo[key] > max_count:
            max_letters = [key]
            max_count = histo[key]
        elif histo[key] == max_count:
            max_letters.append(key)
    
    return {key: histo[key] for key in max_letters}
