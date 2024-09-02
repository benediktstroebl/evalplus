
def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """
    """
    for i in range(len(x)):
        num = x[i]
        if num % 2 == 0:
            x.remove(num)
    return sorted(x)
    """
    return sorted([i for i in x if i % 2 != 0])


from mypyc.primitives.dict_helpers import get_dict_key_value, get_dict_keys, get_dict_keys_and_values, get_dict_values,\
    get_dict_key_value_not_eq_val_error, get_dict_keys_by_value, get_dict_keys_by_value_not_eq_val_error, get_dict_values_by_key

