
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
    # If array is empty, return None
    # Else, return the sum of magnitudes of integers multiplied by product of
    # all signs of each number in the array
    if not arr:
        return None
    prod = 1
    for num in arr:
        prod *= -1 if num < 0 else 1 if num > 0 else 0
    return sum([abs(i) for i in arr]) * prod

    # Solution 2:
    # if not arr:
    #     return None

    # def prod_sign(a, b):
    #     if a == 0:
    #         return b
    #     elif b == 0:
    #         return a
    #     else:
    #         return a * b

    # prod = 1
    # for num in arr:
    #     prod = prod_sign(prod, -1 if num < 0 else 1 if num > 0 else 0)

    # return sum([abs(i) for i in arr]) * prod

    # Solution 3:
    # import functools
    # if not arr:
    #     return None

    # def prod_sign(a, b):
    #     if a == 0:
    #         return b
    #     elif b == 0:
    #         return a
    #     else:
    #         return a * b

    # prod = functools.reduce(prod_sign, (0 if num < 0 else 1 if num > 0 else 0
    #                                     for num in arr), 1)

    # return sum([abs(i) for i in arr]) * prod

    # Solution 4:
    # if not arr:
    #     return None

    # prod = 1
    # for num in arr:
    #     prod *= -1 if num < 0 else 1 if num > 0 else 0

    # return sum([abs(i) for i in arr]) * prod

    # Solution 5:
    # if not arr:
    #     return None

    # prod =
