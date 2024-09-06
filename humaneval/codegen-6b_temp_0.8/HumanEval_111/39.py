
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
    # from collections import Counter
    # hist = Counter(test)
    # max_value = max(hist.itervalues())
    # return dict((key, value) for (key, value) in hist.iteritems() if value == max_value)
    # return histogram_dict
    # histogram_dict = {}
    # for c in test:
    #     if c in histogram_dict:
    #         histogram_dict[c] += 1
    #     else:
    #         histogram_dict[c] = 1
    # max_value = max(histogram_dict.itervalues())
    # returned_dict = {key: value for (key, value) in histogram_dict.iteritems() if value == max_value}
    # return returned_dict
    histogram_dict = {}
    for c in test:
        histogram_dict[c] = histogram_dict.get(c, 0) + 1
    return histogram_dict

