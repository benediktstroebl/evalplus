
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
    sorted_list = sorted(x)
    unique_list = [x[i] for i in range(len(x)) if not any(int(str(n)) % 2 == 0 for n in x[:i+1])]
    return unique_list

