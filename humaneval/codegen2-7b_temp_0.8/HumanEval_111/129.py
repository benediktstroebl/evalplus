
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
    
    if test == "":
        return {}
    
    count = {}
    
    for i in test:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    
    max_value = max(count.values())
    
    for key, value in count.items():
        if value == max_value:
            return {key:value}
    return {}

