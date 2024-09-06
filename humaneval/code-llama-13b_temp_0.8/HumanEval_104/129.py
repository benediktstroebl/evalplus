
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
    new = []
    for i in x:
        if all(int(j) % 2 != 0 for j in str(i)):
            new.append(i)
    return sorted(new)

    # Other solutions:
    # return sorted([x for x in x if not any(int(n) % 2 == 0 for n in str(x))])
    # return sorted(x for x in x if not any(int(n) % 2 == 0 for n in str(x)))
