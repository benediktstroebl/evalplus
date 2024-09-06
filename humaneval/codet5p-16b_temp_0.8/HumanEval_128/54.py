
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

    arr_len = len(arr)
    if arr_len == 0:
        return None
    
    signs = [1] * arr_len
    for i, elem in enumerate(arr):
        signs[i] *= (1 if elem > 0 else -1)
    
    sum_magnitudes = sum(abs(elem) for elem in arr)
    
    return sum_magnitudes * prod_signs(signs)
    
