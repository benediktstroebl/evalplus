
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
    negatives = 0
    products = 1
    for num in arr:
        if num == 0:
            return 0
        elif num < 0:
            negatives += 1
        products *= num
    return abs(products) * (1 if (negatives % 2) else -1)

    # Solution 2
    from functools import reduce
    if not arr:
        return None
    return abs(reduce(lambda x, y: x * y, arr)) * (1 if (arr.count(0) % 2) else -1)
