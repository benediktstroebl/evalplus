
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
    # sort x so that even elements are always at the end
    x.sort()
    # keep track of all non-even elements
    non_even = []
    # iterate through x, for each element
    for i in x:
        # check if the element is even
        if i % 2 == 0:
            # if it is, add it to non_even
            non_even.append(i)
        else:
            # if it isn't, append it to the sorted list
            x.insert(x.index(i)+1, i)
    return non_even
