
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
    n = [int(i) for i in str(x)]
    num = 0
    digits = []
    for i in n:
        if i % 2 == 0:
            num += 1
            continue
        else:
            digits.append(i)
    return sorted(digits)

