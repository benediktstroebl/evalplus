
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

    if not arr: return None
    if len(arr) == 1: return arr[0]
    sum_mag = sum([abs(x) for x in arr])
    sum_sign = sum([x if x == 1 or x == -1 else 0 for x in arr])
    return sum_mag * sum_sign

