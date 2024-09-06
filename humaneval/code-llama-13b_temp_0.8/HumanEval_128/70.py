
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

    signs = 1
    for i in arr:
        signs *= 1 if i > 0 else -1 if i < 0 else 0
    return signs * sum(abs(x) for x in arr)

    # Solution 2
    if not arr:
        return None

    signs = [-1 if x < 0 else 1 if x > 0 else 0 for x in arr]
    return signs[0] * sum(abs(x) for x in arr)

    # Solution 3
    if not arr:
        return None

    signs = sum(x < 0 for x in arr) - sum(x == 0 for x in arr)
    return signs * sum(abs(x) for x in arr)

    # Solution 4
    if not arr:
        return None

    signs = 1
    for i in arr:
        if i > 0:
            signs *= 1
        elif i < 0:
            signs *= -1
    return signs * sum(abs(x) for x in arr)

