
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
    # Sort the list in increasing order (not ascending)
    x.sort(key=lambda x: x, reverse=False)
    # Initialize empty list to hold unique integers
    unique_list = []
    # iterate over the integers
    for num in x:
        # if integer is even, not appended
        if num % 2 == 0:
            continue
        # else, append to list of unique integers
        unique_list.append(num)
    # after iterating through list, return sorted list of integers
    return sorted(unique_list)
