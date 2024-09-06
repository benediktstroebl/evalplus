
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
    d = [int(n) for n in str(x)]
    sorted_digits = sorted(d)
    return [i for i in d if not any(str(i) == str(i).zfill(len(str(i))-1) for _ in range(2))]

