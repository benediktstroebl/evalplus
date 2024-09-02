
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
    # Solution 1:
    if not arr:
        return None
    prod, signs = 1, 0
    for num in arr:
        if not num:
            signs += 1
        elif num > 0:
            prod *= num
            signs += 1
        else:
            prod *= num
            signs -= 1
    return prod * signs


    # Solution 2:
    if not arr:
        return None
    return sum([abs(num) * (-1 if num < 0 else 1) for num in arr]) * abs(reduce(lambda x, y: x * y, arr))
