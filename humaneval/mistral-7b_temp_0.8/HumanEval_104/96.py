
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
    list_s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    result = []
    for i in x:
        for j in range(0, len(i)):
            if i % 10 == 0:
                i = i - i % 10
                list_s.append(i)
            elif i % 10 % 2 == 0:
                i = i - i % 10
                list_s.append(i)
            else:
                result.append(i)
    return result

