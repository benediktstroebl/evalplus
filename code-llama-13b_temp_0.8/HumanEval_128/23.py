
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
    # Solution 1
    prod = 1
    for x in arr:
        prod *= x if x else 1

    sign = 1
    for x in arr:
        sign *= (x > 0) - (x < 0)

    return sign * abs(prod) if prod else None

