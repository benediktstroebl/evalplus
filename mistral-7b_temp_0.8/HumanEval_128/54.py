
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
    if arr:
        # positive if all negative
        if all(x < 0 for x in arr):
            return 1

        # positive if all positive
        elif all(x > 0 for x in arr):
            return -1

        # negative if two positive
        if any(x > 0 for x in arr) and any(x < 0 for x in arr):
            return 0
