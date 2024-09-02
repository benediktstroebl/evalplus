
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
    mult = 1
    for elem in arr:
        mult *= elem
    signs = [1 if elem > 0 else -1 if elem < 0 else 0 for elem in arr]
    return sum([abs(elem) for elem in arr]) * mult * signs[0]
    
