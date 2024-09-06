
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
    #return [x for x in unique_digits(x) if not any(map(lambda y: y%2 == 0, map(int, str(x))))]
    if x == []:
        return []
    x.sort()
    unique_lst = [x[0]]
    for i in range(1, len(x)):
        if x[i] != x[i - 1]:
            unique_lst.append(x[i])
    unique_lst.sort()
    return unique_lst
