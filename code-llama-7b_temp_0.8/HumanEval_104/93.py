
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
    if not x:
        return []

    seen = set()
    seen_add = seen.add
    result = []
    for num in x:
        if any(i in seen for i in str(num)):
            continue

        seen_add(num)
        result.append(num)

    return sorted(result)

