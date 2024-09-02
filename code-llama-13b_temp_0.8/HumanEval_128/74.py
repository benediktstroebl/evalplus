
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
    # Solution uses helper function which recursively builds the signs product
    # and returns the sum of magnitudes multiplied by the product of signs
    if not arr:
        return None
    signs = 1
    for item in arr:
        if item != 0:
            signs *= -1 if item < 0 else 1
    return sum(abs(item) for item in arr) * signs

