
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
    # Solution 1
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            prod = 0
        elif num < 0:
            prod = -prod
    s = 0
    for num in arr:
        s += num * prod
    return s

    # Solution 2
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            prod = 0
        elif num < 0:
            prod *= -1
    return sum(num * prod for num in arr)

    # Solution 3
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            prod = 0
        elif num < 0:
            prod = -prod
    return sum(num * prod for num in arr)

    # Solution 4
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            prod = 0
        elif num < 0:
            prod *= -1
    return sum(num * prod for num in arr)

    # Solution 5
    if not arr:
        return None
    prod = 1
    for num in arr:
        if num == 0:
            prod = 0
        elif num < 0:
            prod = -prod
    return sum(num * prod for num in arr)

