
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

    signs = [0] * len(arr)
    for i, elem in enumerate(arr):
        if elem > 0:
            signs[i] = 1
        elif elem < 0:
            signs[i] = -1
        else:
            signs[i] = 0

    sign_prod = 1
    for sign in signs:
        sign_prod *= sign

    signs_abs = [abs(elem) for elem in arr]
    signs_abs_prod = 1
    for elem in signs_abs:
        signs_abs_prod *= elem

    return signs_abs_prod * sign_prod
