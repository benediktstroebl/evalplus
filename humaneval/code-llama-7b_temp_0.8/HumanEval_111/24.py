
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
    # my solution
    # d = {}
    # for i in test:
    #     if i not in d:
    #         d[i] = 1
    #     else:
    #         d[i] += 1
    # return d

    # l = test.split()
    # d = {}
    # for i in l:
    #     d[i] = d.get(i, 0) + 1
    # return d
    # return dict((i, l.count(i)) for i in set(l))

    # other solution
    from collections import defaultdict

    d = defaultdict(int)
    for i in test:
        d[i] += 1
    return d

