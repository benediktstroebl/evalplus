
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
    # Solution 1:
    if not arr:
        return None
    signs = [i//abs(i) for i in arr]
    signs.remove(0)
    signs_prod = 1
    for i in signs:
        signs_prod *= i
    return sum([abs(i) * signs_prod for i in arr])

    # Solution 2:
    # signs = [i//abs(i) for i in arr]
    # signs_prod = 1
    # for i in signs:
    #     if i:
    #         signs_prod *= i
    # return sum([abs(i) * signs_prod for i in arr])

