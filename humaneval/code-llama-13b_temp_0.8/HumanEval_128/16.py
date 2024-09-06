
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
    if len(arr) == 0:
        return None

    prod_signs = 1
    for num in arr:
        if num != 0:
            prod_signs *= 1 if num > 0 else -1

    magnitudes = [abs(num) for num in arr]
    return sum(magnitudes) * prod_signs

    # Solution 2
    if not arr:
        return None

    prod = 1
    s = 0
    for num in arr:
        prod *= 1 if num > 0 else -1
        if num != 0:
            s += abs(num)

    return s * prod

    # Solution 3
    prod_sign = 1
    for num in arr:
        if num:
            prod_sign *= 1 if num > 0 else -1
    return sum(abs(num) for num in arr) * prod_sign if arr else None
