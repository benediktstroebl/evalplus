
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
    # Solution:
    prod = 1
    signs = 0
    for i in arr:
        signs += int(i > 0) - int(i < 0)
        prod *= i
    return None if prod == 0 else prod * signs

    # Solution 2:
    # >>> return None if not arr else reduce(lambda x, y: x * y, arr) * reduce(lambda x, y: x + y, map(lambda x: 1 if x > 0 else -1 if x < 0 else 0, arr))
