
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
    # Solution using reduce and operator
    # import operator
    # from functools import reduce
    # if not arr:
    #     return None
    # # return reduce(lambda x, y: x * y, map(lambda z: 1 if z > 0 else 0 if z == 0 else -1, arr)) * reduce(lambda x, y: x * y, arr)
    # return reduce(operator.mul, map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr)) * reduce(operator.mul, arr)
    # Solution using sum and lambda
    if not arr:
        return None
    return sum(map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr)) * prod(arr)

