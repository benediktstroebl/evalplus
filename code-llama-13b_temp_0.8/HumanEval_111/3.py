
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
    
    histogram = {}
    words = test.split()
    for word in words:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    count = 0
    max_key = []
    for key, val in histogram.items():
        if val > count:
            count = val
            max_key = [key]
        elif val == count:
            max_key.append(key)
    return {i: histogram[i] for i in max_key}
            
            
            
