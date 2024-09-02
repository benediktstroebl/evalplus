
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
    # solution 1
    if len(arr) == 0:
        return None
    signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
    signs_prod = 1
    for i in signs:
        signs_prod *= i
    arr_abs = [abs(i) for i in arr]
    arr_abs_prod = 1
    for i in arr_abs:
        arr_abs_prod *= i
    return signs_prod * arr_abs_prod

