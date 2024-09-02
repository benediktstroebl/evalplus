
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
    # you code here
    result = []
    for elem in x:
        if elem < 10:
            result.append(elem)
        else:
            if elem % 2 == 1:
                result.append(elem)
    return sorted(result)

test(unique_digits([15, 33, 1422, 1]), [1, 15, 33])
test(unique_digits([152, 323, 1422, 10]), [])
test(unique_digits([1, 2, 3]), [1, 2, 3])
test(unique_digits([2, 4, 6]), [2, 4, 6])
test(unique_digits([4, 16, 64, 28, 256]), [4, 16, 64, 28, 256])
