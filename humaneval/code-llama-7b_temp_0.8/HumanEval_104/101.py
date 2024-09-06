
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
    # Convert to string
    x = list(map(str, x))
    # get unique elements
    x_unique = list(set(x))
    # get elements that doesn't have any even digit
    even_digits = [1, 3, 5, 7, 9]
    x_unique_filtered = []
    for i in x_unique:
        if all(d in even_digits for d in i):
            x_unique_filtered.append(i)
    x_unique_filtered.sort()
    return x_unique_filtered

