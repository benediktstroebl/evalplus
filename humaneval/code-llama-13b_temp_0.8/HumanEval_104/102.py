
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

    res = []
    for elem in x:
        if elem < 0:
            continue
        has_even_digit = False
        while elem > 0:
            last_digit = elem % 10
            if last_digit % 2 == 0:
                has_even_digit = True
                break
            elem //= 10
        if not has_even_digit:
            res.append(elem)
    return sorted(res)
