
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

    signs = [1, -1, 0]
    for i in range(len(arr)):
        signs = [signs[j]*arr[i] for j in range(len(arr)) if signs[j] != 0]
    product = [sum(x) for x in signs]
    return sum(x*y for x, y in zip(product, signs))