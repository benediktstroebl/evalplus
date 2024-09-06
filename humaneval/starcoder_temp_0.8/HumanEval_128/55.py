
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
    # My solution
    # def prod(arr):
    #     res = 1
    #     for a in arr:
    #         res *= a
    #     return res

    # if len(arr) == 0:
    #     return None
    # else:
    #     res = 0
    #     for a in arr:
    #         if a > 0:
    #             res += a
    #         elif a < 0:
    #             res += -a
    #         else:
    #             res += 0
    #     return prod(arr) * res

    # Another solution
    if not arr:
        return None

    sum_signs = sum(1 if x > 0 else (-1 if x < 0 else 0) for x in arr)
    return sum(abs(x) * sum_signs for x in arr)
