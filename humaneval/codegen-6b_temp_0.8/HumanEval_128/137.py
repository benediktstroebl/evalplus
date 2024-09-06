
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
    if len(arr) == 0:
        return None

    multiply_by_sign = lambda x: x * sign(x)
    return sum(map(multiply_by_sign, arr))


assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) is None
assert prod_signs([3, 1, -3, 5, -2]) == -20
assert prod_signs([-1, 2, 4, -2, -1]) == -5
assert prod_signs([-1, -2, -3, -3]) == 0
assert prod_signs([2, -3, -1, 2]) == -5
