
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
    import numpy as np
    if not arr:
        return None
    return np.sum(np.abs(arr)) * np.prod([0, *map(lambda x: -1 if x < 0 else 1, arr)])

    # Solution using itertools
    from itertools import accumulate, repeat, chain
    if not arr:
        return None
    return sum(map(abs, arr)) * prod(chain((1,), repeat(1, arr.count(0)), (-1,), repeat(-1, arr.count(-1))))

    # Solution using math.prod
    import math
    if not arr:
        return None
    return sum(map(abs, arr)) * math.prod(chain((1,), repeat(1, arr.count(0)), (-1,), repeat(-1, arr.count(-1))))

    # Solution using functools.reduce
    from functools import reduce
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(lambda x, y: x * (1 if y > 0 else -1), arr, 1)

    # Solution using more list comprehensions
    if not arr:
        return None
    return sum(map(abs, arr)) * prod([1 if x > 0 else -1 for x in arr if x])

    # Solution using operator.mul
    from operator import mul
    import itertools as it
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(mul, (1 if x > 0 else -1 for x in arr if x), 1)

    # Solution using reduce
    from functools import reduce
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(lambda x, y: x * (1 if y > 0 else -1), arr, 1)

    # Solution using lambda
    if not arr:
        return None
    return sum(map(abs, arr)) * reduce(lambda x, y: x * (1 if y > 0 else -1), arr, 1)

    # Solution using only sum
    
