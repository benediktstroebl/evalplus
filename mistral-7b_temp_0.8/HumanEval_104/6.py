
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
    
    if isinstance(x, int):
        x = [x]
    
    x = sorted(x)
    e = [i for i in x if all(x[0] % 10 != y for y in x if x[0] != y)]
    o = [i for i in x if all(x[0] % 10 == y for y in x if x[0] != y)]
    if e == [] and o == []:
        return []
    if e != []:
        return e
    return o
