
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
    elif arr[0] > 0:
        return abs(arr[0]) * sum(arr[1:]) * prod_signs(arr[1:])
    elif arr[0] == 0:
        return prod_signs(arr[1:])
    else:
        return -abs(arr[0]) * sum(arr[1:]) * prod_signs(arr[1:])
