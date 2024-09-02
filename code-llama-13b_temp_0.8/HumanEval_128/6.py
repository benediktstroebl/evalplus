
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
    # Solution using NumPy
    # import numpy as np
    # return np.sum(np.abs(arr) * np.prod(np.sign(arr)))

    # Solution using math.prod()
    import math

    if not arr:
        return None
    return sum(abs(x) * math.prod([1, -1] * (x != 0)) for x in arr)

