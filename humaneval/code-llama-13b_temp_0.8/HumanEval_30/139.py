

def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """
    # 3 if-clause
    # 1 for-clause
    # 1 list-append
    # 1 function-call
    # 4 return
    # 1 list-comprehension
    # 4 other
    result = []
    for item in l:
        if item > 0:
            result.append(item)
    return result

