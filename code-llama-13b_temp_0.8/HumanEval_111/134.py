
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
    
    word = test.split()
    word = [x.lower() for x in word]
    word = list(set(word))
    dct = {}
    
    for i in word:
        dct[i] = word.count(i)

    max_occurence = max(dct.values())
    dct2 = {}
    
    for key, value in dct.items():
        if value == max_occurence:
            dct2[key] = value
            
    return dct2
    
