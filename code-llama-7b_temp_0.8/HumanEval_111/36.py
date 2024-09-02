
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
    test_list = test.split(" ")
    if test_list == ['']:
        return {}
    else:
        test_dict = {}
        for item in test_list:
            if item not in test_dict.keys():
                test_dict[item] = test_list.count(item)
            else:
                test_dict[item] += test_list.count(item)
        return test_dict
