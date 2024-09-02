
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
    if arr:
        s = sum(abs(i) * i for i in arr)
        if len(arr) == 1:
            return s * 1
        m = len(arr)
        prod = 1
        for i in arr:
            if i > 0:
                prod *= 1
            else:
                prod *= -1
        return (s * prod) % (10 ** 9 + 7)
    else:
        return None




