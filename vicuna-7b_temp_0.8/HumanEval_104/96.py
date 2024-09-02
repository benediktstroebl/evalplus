
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
    low = 0
    high = len(x) - 1
    while low <= high:
        mid = (low + high) // 2
        digit = x[mid] % 2
        if digit != 0:
            low = mid + 1
        else:
            high = mid
    return x[low:high+1]
