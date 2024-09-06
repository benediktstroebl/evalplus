
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
    n = 0
    count = Counter([int(j) % 10 for j in x])
    result = []
    for i in range(10):
        if count[i] % 2 == 0:
            continue
        if count[i] != 0:
            result.append(i)
            count[i] += 1
    return sorted(result)
