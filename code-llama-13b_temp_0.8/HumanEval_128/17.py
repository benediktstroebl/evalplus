
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
    # Solution 1:
    if not arr:
        return None

    p_sign = 1
    p_mult = 1
    for n in arr:
        if n:
            p_mult *= n
        if n > 0:
            p_sign *= 1
        if n < 0:
            p_sign *= -1
    return abs(p_mult) * p_sign

    # Solution 2:
    if not arr:
        return None

    p_sign = 1
    p_mult = 1
    for n in arr:
        if n:
            p_mult *= n
        if n > 0:
            p_sign *= 2
        if n < 0:
            p_sign *= -2
    return abs(p_mult) * p_sign // 4

