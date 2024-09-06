
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
    product = 1
    for i in range(len(arr)):
        sign = arr[i]
        if sign == 1:
            product *= i
        elif sign == -1:
            product *= (len(arr)-i-1)
        else:
            product *= 0
    return product * sum(map(abs, arr))
