
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
    if arr == []:
        return None
    product_signs = 1
    sum_magnitudes = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            product_signs *= arr[i] / abs(arr[i])
            sum_magnitudes += abs(arr[i])
    return sum_magnitudes * product_signs

