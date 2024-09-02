
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
    # Your code here
    if test == "":
        return {}
    else:
        test_dict = {}
        for i in test.split(" "):
            if i in test_dict:
                test_dict[i] += 1
            else:
                test_dict[i] = 1
    max_val = max(test_dict.values())
    final_dict = {}
    for i in test_dict:
        if test_dict[i] == max_val:
            final_dict[i] = test_dict[i]
    return final_dict
