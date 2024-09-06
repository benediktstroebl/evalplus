
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
    try:
        from collections import defaultdict
    except:
        print('collections.defaultdict not available')
    
    histogram_dict = defaultdict(int)
    
    if test:
        for char in test.split():
            histogram_dict[char] += 1

    max_val = max(histogram_dict.values())
    return dict((k, v) for k, v in histogram_dict.items() if v == max_val)
