
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
    return sum([abs(x) for x in arr]) * prod([1, -1][x < 0] for x in arr)


    # Solution 2
    # prod_sign = 1
    # for num in arr:
    #     if num == 0:
    #         return None
    #     elif num < 0:
    #         prod_sign *= -1
    # return sum([abs(x) for x in arr]) * prod_sign


    # Solution 3
    # def is_zero(arr):
    #     for elem in arr:
    #         if elem < 0:
    #             return -1
    #         elif elem > 0:
    #             return 1
    #     return 0

    # def prod_sign(arr):
    #     """Returns product of signs of all elements"""
    #     return reduce(lambda x, y: x * y, [1, -1][num < 0] for num in arr)

    # def prod_abs(arr):
    #     """Returns sum of magnitudes of all elements"""
    #     return reduce(lambda x, y: x + y, map(abs, arr))

    # return prod_abs(arr) * prod_sign(arr)
