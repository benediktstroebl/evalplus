
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
    hist = {}
    l = len(test)
    for i in range(l):
        if test[i] in hist:
            hist[test[i]] += 1
        else:
            hist[test[i]] = 1
            
    max = 0
    result = []
    for key in hist:
        if hist[key] > max:
            max = hist[key]
            result = [key]
        elif hist[key] == max:
            result.append(key)
    return {x: hist[x] for x in result}
        
