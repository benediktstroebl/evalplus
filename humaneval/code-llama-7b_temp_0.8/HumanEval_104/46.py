
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
    result = []
    visited = set()
    for item in x:
        visited.add(item)
        current = item
        while current:
            if current % 10 % 2 == 0:
                visited.remove(item)
                break
            else:
                current //= 10
    return sorted(visited)


