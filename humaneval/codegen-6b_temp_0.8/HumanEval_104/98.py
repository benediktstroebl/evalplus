
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
    """
    1. Take all the numbers from x and put them in a set to simplify the code
    2. for each number in x, if it has an even digit, remove it from the set
    3. at the end, return a sorted list of the set
    """
    x = set(x)
    for i in x:
        if i % 2 == 0:
            x.remove(i)
    return sorted(list(x))
