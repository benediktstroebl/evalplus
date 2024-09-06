
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

    ls = []

    for num in x:
        if num >= 10:
            if num % 2 != 0:
                ls.append(num)

        elif num >= 5:
            if num % 2 != 0:
                ls.append(num)

    if ls == []:
        return []

    else:
        ls.sort()
        return ls

