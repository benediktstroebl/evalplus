
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
    if len(arr) == 1:
        return arr[0]
    
    if arr[0] == 0:
        return 0

    product = 1
    sum_magnitudes = 0
    
    for i in range(len(arr)):
        if arr[i] == 0:
            continue
        
        sum_magnitudes += abs(arr[i])
        if arr[i] > 0:
            product *= 1
        else:
            product *= -1
        
    return product * sum_magnitudes
