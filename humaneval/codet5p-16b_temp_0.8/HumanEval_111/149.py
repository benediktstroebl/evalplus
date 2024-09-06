
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

    

    a = test.split(' ')
    b = {}

    for i in a:
        if i in b:
            b[i] += 1
        else:
            b[i] = 1

    max_ = max(b.values())
    return {k:v for k,v in b.items() if v == max_}
    
    
    
    

