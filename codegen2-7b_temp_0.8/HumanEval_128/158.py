
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
    for i, v in enumerate(arr):
        if v == 0:
            signs[i] = 0
        elif v > 0:
            signs[i] = 1
        elif v < 0:
            signs[i] = -1
    return sum([i * j for i, j in zip(arr, signs)
