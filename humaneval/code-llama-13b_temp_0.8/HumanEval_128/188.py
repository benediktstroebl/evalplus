
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
    arr_sign = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
    arr_abs = [abs(i) for i in arr]
    arr_prod = reduce(lambda x, y: x*y, arr_sign, 1)
    return sum(arr_abs)*arr_prod

    # Solution 2
    from functools import reduce
    if not arr:
        return None
    from math import prod
    prod_sign = prod(map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr))
    arr_abs = [abs(i) for i in arr]
    return sum(arr_abs) * prod_sign

    # Solution 3
    if not arr:
        return None
    from functools import reduce
    from operator import mul
    prod_sign = reduce(mul, map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr))
    return sum(map(abs, arr)) * prod_sign

