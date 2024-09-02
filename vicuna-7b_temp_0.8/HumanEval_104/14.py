
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
    # sort the list
    x = sorted(x)
    # reverse the list
    x = x[::-1]
    # check if the list is empty
    if len(x) == 0:
        return []
    # use a counter to keep track of the number of odd digits
    count = 0
    result = []
    for i in x:
        # check if the number is odd
        if i % 2 == 1:
            count += 1
        else:
            result.append(i)
    return result
