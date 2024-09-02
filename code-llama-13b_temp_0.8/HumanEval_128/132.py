
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
    # Solution 1
    if arr == []:
        return None

    prod = 1
    signs = []
    for n in arr:
        signs.append(n // abs(n))
        prod *= n
    signs.sort()

    return prod * signs[-1]


    # Solution 2
    from itertools import accumulate
    from functools import reduce

    if arr == []:
        return None

    return reduce(
        lambda x, y: x * y,
        accumulate(arr, lambda x, y: 1 if x == y else x * y, initial=1),
    )
