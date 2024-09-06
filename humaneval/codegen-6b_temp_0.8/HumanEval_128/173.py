
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

    sum = 0
    for i in range(arr_len):
        if arr[i] == 0:
            continue
        elif arr[i] > 0:
            sum += arr[i]
        elif arr[i] < 0:
            sum -= arr[i]
    return sum
