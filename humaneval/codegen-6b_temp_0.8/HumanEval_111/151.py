
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
    for c in test:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d

"""
Given a string, we'll say that the front is the first 3 chars of the string. 
If the string length is less than 3, 
the front is whatever is there. 
Return a new string which is 3 copies of the front.

front3('Java') => 'JavJavJav'
front3('Chocolate') => 'ChoChoCho'
front3('abc') => 'abcabcabc'
"""