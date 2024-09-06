
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
    # Your code here
    digits = []
    for x in x:
        digits.append(str(x))
    unique = []
    for x in digits:
        for y in x:
            if int(y) % 2 == 0:
                break
        else:
            unique.append(int(x))
    return sorted(unique)

