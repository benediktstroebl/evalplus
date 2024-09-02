
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
    
    d = {}
    t = test.split()
    for i in t:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    print(d)
    for i in d:
        if i[1] == d[0][1]:
            return {i[0]}
    return {i[0] for i in d}

