
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

    # return None for empty arr
    if not arr:
        return None

    # Find sign of each number
    # Find product of all signs
    # Find sum of magnitudes of integers multiplied by product of all signs

    signs = [1 if a > 0 else -1 if a < 0 else 0 for a in arr]
    sign_prod = reduce((lambda x, y: x * y), signs)
    return sign_prod * sum(abs(a) for a in arr)

