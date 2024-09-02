
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

    signs = []
    for el in arr:
        signs.append(1 if el>0 else -1 if el<0 else 0)
    return sum(abs(el) for el in arr) * prod_signs(signs) if len(arr)>0 else None


