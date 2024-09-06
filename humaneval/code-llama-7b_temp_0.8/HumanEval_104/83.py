
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
    unique = []
    for i in range(len(x)):
        for j in range(len(str(x[i]))):
            if int(str(x[i])[j]) % 2 == 0 and x[i] not in unique:
                break
            elif int(str(x[i])[j]) % 2 != 0 and x[i] not in unique:
                unique.append(x[i])
                break
    return sorted(unique)
