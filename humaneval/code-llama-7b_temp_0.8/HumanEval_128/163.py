
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
    if not arr[0]:
        return 0
    # [a, b, c, ...]
    # [1, 1, 1, ...]
    # [0, 0, 0, ...]
    signs = [1] * len(arr)
    for i, num in enumerate(arr):
        if num < 0:
            signs[i] = -1
    return prod_of_array(arr) * sum(signs)

