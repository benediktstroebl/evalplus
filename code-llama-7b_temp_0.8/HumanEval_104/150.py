
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
    # My solution:
    # return [i for i in x if not any(map(lambda i: i % 2 == 0, str(i)))]
    
    # faster solution:
    if not x:
        return []

    return [n for n in x if not any(map(lambda i: i % 2 == 0, str(n)))]
    
    # Solution by David:
    return [n for n in x if not any(n % 2 == 0 for i in str(n))]
    
    # Solution by Shaurya:
    return [n for n in x if not any(int(i) % 2 == 0 for i in str(n))]

