
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
    # get all items with even digits
    evens = [str(x) for x in x if x % 2 == 0]
    # get all items with odd digits
    odds = [str(x) for x in x if x % 2 != 0]
    # combine items with evens and odds
    odds.extend(evens)
    # sort
    odds.sort()
    return odds

