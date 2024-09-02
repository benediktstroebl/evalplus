
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

    sign = lambda x: 0 if x == 0 else x // abs(x)

    signs = [sign(x) for x in arr]
    signs_prod = 1
    for s in signs:
        signs_prod *= s

    signs_abs = [abs(x) for x in arr]
    signs_abs_prod = 1
    for s in signs_abs:
        signs_abs_prod *= s

    return signs_prod * signs_abs_prod
