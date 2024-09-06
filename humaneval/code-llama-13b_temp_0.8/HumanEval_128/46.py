
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
    product = 1
    for x in arr:
        if x < 0:
            product *= -1
        if x > 0:
            product *= 1
        if x == 0:
            product *= 1
    return sum(arr) * product

    # Solution 2
    from math import prod
    return sum(arr) * prod(1 if x > 0 else -1 for x in arr)

    # Solution 3
    # product = 1
    # count = 0
    # for i in arr:
    #     if i == 0:
    #         count += 1
    #     if i > 0:
    #         product *= 1
    #     if i < 0:
    #         product *= -1
    # if count != 0:
    #     return None
    # return sum(arr) * product

    # Solution 4
    # if not arr:
    #     return None
    # neg, pos = 0, 0
    # for x in arr:
    #     if x == 0:
    #         neg += 1
    #         pos += 1
    #     if x > 0:
    #         pos += 1
    #     if x < 0:
    #         neg += 1
    # if neg > 0 and pos > 0:
    #     return None
    # return sum(arr) * (-1 if neg > pos else 1)

    # Solution 5
    # def f(arr):
    #     product = 1
    #     for x in arr:
    #         if x == 0:
    #             return None
    #         if x < 0:
    #             product *= -1
    #         if x > 0:
    #             product *= 1
    #     return product
    # return sum(arr) * f(arr)

    # Solution 6
    # return sum(arr) * ((-1) ** (len([x for x in arr if x < 0])))
