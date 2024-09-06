
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

    product = 1
    signs = []
    for elem in arr:
        if elem != 0:
            signs.append(elem // abs(elem))
            product *= elem
        else:
            signs.append(0)
    signs.remove(0)

    prod_signs = 0
    for sign in signs:
        prod_signs += sign

    return abs(prod_signs) * product

