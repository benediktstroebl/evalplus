
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
    # in one line
    return {k:v for k,v in sorted(test.split(' '), key=lambda x:test.count(x))}

    # with counting
    # from collections import Counter
    # return Counter(test)

    # other solution
    # def histogram(test):
    #     return dict(test.split())

    # yet another solution
    # return dict([(a, test.count(a)) for a in test.split()])

