
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
    s = test.split()
    n = len(s)
    d = {}
    cnt = {}
    for i in range(n):
        c = s[i].lower()
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
    for c in cnt:
        d[c] = cnt[c]
    return d
