
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

    
    test = test.split()
    test = list(map(str, test))

    if len(test) == 0:
        return {}
    
    s = test[0]
    h = { s : 1 }
    for word in test:
        if word in h:
            h[word] += 1
        else:
            h[word] = 1

    max_value = max(h.values())
    max_letter = ''
    for letter, value in h.items():
        if value == max_value:
            max_letter = letter
    
    return {max_letter : max_value}
    
