
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
    arr_copy = arr[:]
    prod = 1
    for i in range(len(arr_copy)):
        if arr_copy[i] < 0:
            prod *= -1
        arr_copy[i] *= prod
    return sum([abs(x) for x in arr_copy]) * prod

