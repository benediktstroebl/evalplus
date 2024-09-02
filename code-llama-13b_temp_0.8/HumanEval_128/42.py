
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
    # Solution using numpy:
    # if len(arr) > 0:
    #     return np.sum(np.abs(arr)) * np.prod([x / abs(x) for x in arr])
    # return None

    # Solution using math:
    if len(arr) > 0:
        total = sum(abs(x) for x in arr)
        prod = 1
        for x in arr:
            if x != 0:
                prod *= x / abs(x)
        return total * prod
    return None

