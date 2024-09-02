
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
    x = [int(i) for i in str(x)]
    x = sorted(x)
    for i in range(len(x)):
        for j in range(i+1, len(x)):
            if sum(map(lambda n: n % 2 == 0, x[i:j])) == 0:
                x.remove(x[i])
                x.remove(x[j])
    return x
