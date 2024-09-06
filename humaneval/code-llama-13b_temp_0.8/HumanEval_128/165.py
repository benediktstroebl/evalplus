
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
    if not arr:
        return None
    sign_arr = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    signs_prod = 1
    for x in sign_arr:
        signs_prod *= x
    signs_abs = [abs(x) for x in arr]
    signs_abs_prod = 1
    for x in signs_abs:
        signs_abs_prod *= x
    return signs_abs_prod * signs_prod

