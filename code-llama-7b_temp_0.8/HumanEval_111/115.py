
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
    from collections import defaultdict
    my_dict = defaultdict(int)
    my_dict_ret = {}
    for i in test.split(' '):
        my_dict[i] += 1
    for key, value in my_dict.items():
        if value == max(my_dict.values()):
            my_dict_ret[key] = value
    return my_dict_ret
