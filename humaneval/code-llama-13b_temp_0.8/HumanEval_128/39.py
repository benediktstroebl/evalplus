
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
    # product of sign = -1 if arr has neg, 1 if has pos, 0 otherwise
    product = -1 if any(i < 0 for i in arr) else 1 if any(i > 0 for i in arr) else 0
    # sum of magnitudes = sum of arr with absolute values
    return sum(abs(i) for i in arr) * product if arr else None

