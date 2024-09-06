
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
    else:
        test = test.split(" ")
        my_dict = {}
        for k in test:
            if k not in my_dict.keys():
                my_dict[k] = 1
            else:
                my_dict[k] += 1
        #print(my_dict)
        max_value = max(my_dict.values())
        print(max_value)
        max_key = {k for k, v in my_dict.items() if v == max_value}
        print(max_key)
        return {k: v for k, v in my_dict.items() if v == max_value}
