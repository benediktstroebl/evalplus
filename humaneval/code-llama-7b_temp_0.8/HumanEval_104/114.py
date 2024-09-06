
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
    # Your code here
    result = []
    for num in x:
        num_string = str(num)
        num_string_as_list = [x for x in num_string]
        num_string_as_list_unique = set(num_string_as_list)
        for item in num_string_as_list:
            if '0' in num_string_as_list or '2' in num_string_as_list or '4' in num_string_as_list or '6' in num_string_as_list or '8' in num_string_as_list:
                break
        else:
            if num_string_as_list_unique == set(num_string):
                result.append(num)
    return result

