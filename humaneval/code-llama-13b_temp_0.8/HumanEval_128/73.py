
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
    if not arr:
        return None
    prod_sgn = 1
    for elem in arr:
        if elem == 0:
            prod_sgn = 0
        elif elem < 0:
            prod_sgn *= -1
    return sum(abs(elem) for elem in arr) * prod_sgn

    # Solution 2
    if not arr:
        return None
    abs_arr = sum(abs(num) for num in arr)
    if not abs_arr:
        return 0
    if sum(num < 0 for num in arr) % 2:
        return abs_arr * -1
    return abs_arr

