
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
    # we know that the number of negative integers in the array is odd
    # if prod_signs == -1 then sign of the integer is -1
    # if prod_signs == 1 then sign of the integer is 1
    # if prod_signs == 0 then sign of the integer is 0
    if not arr:
        return None
    prod = 1
    total = 0
    for x in arr:
        if x > 0:
            prod *= 1
        elif x < 0:
            prod *= -1
        else:
            prod *= 0
        total += x * prod
    return total
