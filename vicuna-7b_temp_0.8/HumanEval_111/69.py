
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
    lines = test.split("\n")
    d = {}
    for l in lines:
        if l:
            for i in range(len(l)):
                if l[i].isalpha():
                    d[l[i]] = d.get(l[i], 0) + 1
    max_val = max(d.values())
    d = {v: d[v] for v in d}
    return dict(enumerate(d))