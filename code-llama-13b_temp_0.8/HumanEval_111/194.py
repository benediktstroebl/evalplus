
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
    items = test.split(' ')
    max_key = ''
    max_val = 0
    vals = {}
    for item in items:
        if item in vals:
            vals[item] += 1
        else:
            vals[item] = 1
        if vals[item] > max_val:
            max_val = vals[item]
            max_key = item
    return {key:val for key, val in vals.items() if val == max_val}
    
