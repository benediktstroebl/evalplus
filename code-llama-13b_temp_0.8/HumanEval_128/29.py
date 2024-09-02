
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

    prod = 1
    for num in arr:
        prod *= num

    if prod < 0:
        sign = -1
    elif prod > 0:
        sign = 1
    else:
        return 0

    return sum(abs(num) * sign for num in arr)

