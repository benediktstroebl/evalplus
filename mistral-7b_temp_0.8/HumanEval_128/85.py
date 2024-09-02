
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
    signs = []
    summ = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            signs.append(1)
        elif arr[i] < 0:
            signs.append(-1)
        else:
            signs.append(0)
    if arr == []:
        return None
    for i in range(len(signs)):
        if arr[i] != 0:
            summ += abs(arr[i]) * signs[i]
    return summ
