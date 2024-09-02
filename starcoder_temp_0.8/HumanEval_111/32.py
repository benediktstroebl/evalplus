
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
    max_count = 1

    for i in test.split():
        if i in hist:
            hist[i] += 1
            max_count = max(max_count, hist[i])
        else:
            hist[i] = 1
            max_count = max(max_count, 1)

    result = [i for i in hist if hist[i] == max_count]

    return result if len(result) > 1 else result[0]

