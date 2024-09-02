
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
    # Solution using numpy
    # import numpy as np
    # if not arr:
    #     return None
    # return np.prod(np.abs(arr)) * np.prod(np.sign(arr))
    # Solution using reduce
    from functools import reduce
    if not arr:
        return None
    abs_arr = [abs(x) for x in arr]
    signs = [1 if x > 0 else 0 if x == 0 else -1 for x in arr]
    return reduce(lambda a, x: a * x, abs_arr) * reduce(lambda a, x: a * x, signs)

