
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
    if len(arr) == 0:
        return None
    prod, res = 1, 0
    for num in arr:
        if num == 0:
            continue
        prod *= 1 if num > 0 else -1
        res += abs(num)
    return prod * res

    # Solution 2
    if len(arr) == 0:
        return None
    res = 0
    prod = 1
    for num in arr:
        res += abs(num) * prod
        prod *= -1 if num < 0 else 1
    return res

