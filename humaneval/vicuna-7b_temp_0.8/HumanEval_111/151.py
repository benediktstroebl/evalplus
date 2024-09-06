
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
    s = list(test)
    m, n = len(s), len(s[0])
    d = {}
    for i in range(m):
        for j in range(n):
            if s[i][j] in d:
                d[s[i][j]] += 1
            else:
                d[s[i][j]] = 1
    for k, v in d.items():
        if v > 1:
            yield k, v
            if k in d:
                for i in range(m):
                    for j in range(n):
                        if d[k] > d[s[i][j]] and s[i][j] in d:
                            d[s[i][j]] -= d[k]
                            d[k] = d[s[i][j]]
