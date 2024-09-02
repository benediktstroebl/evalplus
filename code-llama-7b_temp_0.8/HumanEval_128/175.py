
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
    
    signs = [0 if not x else 1 if x > 0 else -1 for x in arr]
    signs_mul = 1
    for s in signs:
        signs_mul *= s
    nums_mul = 1
    for n in arr:
        nums_mul *= n
    return nums_mul * signs_mul
