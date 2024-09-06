
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

    lst = []
    for num in x:
        num_lst = list(str(num))
        for i in num_lst:
            if int(i) % 2!= 0:
                lst.append(num)
                break
    return sorted(lst)
