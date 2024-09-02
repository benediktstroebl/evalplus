
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
    result = 1
    positive = 0
    negative = 0
    zero = 0
    for num in arr:
        if num > 0:
            positive += 1
        elif num < 0:
            negative += 1
        else:
            zero += 1
    result *= (positive % 2) * 2 - 1
    result *= (negative % 2) * 2 - 1
    return result * (positive * negative * zero)
