
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
    n = len(x)
    if n == 0:
        return []
    else:
        for i in range(1, n):
            for j in range(i+1, n):
                if (x[i] % 2 == 0 and x[j] % 2 != 0 or\
                    x[i] % 2 != 0 and x[j] % 2 == 0):
                    break
            else:
                return [x[i]]
