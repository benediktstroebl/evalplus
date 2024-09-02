
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
    elif len(arr) == 1:
        return arr[0]
    else:
        if arr[0] != 0:
            for i in range(1, len(arr)):
                if arr[i] != 0 and arr[i] * arr[0] < 0:
                    return None
                elif arr[i] != 0 and arr[i] * arr[0] > 0:
                    continue
                elif arr[i] == 0:
                    return None
        else:
            return None
        return arr[0] * sum(arr)
