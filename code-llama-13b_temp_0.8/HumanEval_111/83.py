
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
    if len(test) == 0:
        return {}
    else:
        temp_dict = {}
        temp_list = list(test)
        for i in temp_list:
            if i not in temp_dict:
                temp_dict[i] = 1
            else:
                temp_dict[i] += 1
        max_val = max(temp_dict.values())
        final_dict = {}
        for k,v in temp_dict.items():
            if v == max_val:
                final_dict[k] = v
            else:
                pass
        return final_dict
