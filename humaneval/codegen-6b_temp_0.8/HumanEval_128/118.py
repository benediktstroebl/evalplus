
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
    signs = [1] * len(arr)
    for i in range(len(arr)):
        if arr[i] == 0:
            signs[i] = 0
        elif arr[i] > 0:
            signs[i] = 1
        else:
            signs[i] = -1
    return sum(map(abs, arr)) * sum(signs)

