
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
    uniques = set()
    for n in x:
        while n > 0:
            digit = n % 10
            if digit % 2 == 1:
                uniques.add(n)
                break
            n //= 10
    return sorted(uniques)
