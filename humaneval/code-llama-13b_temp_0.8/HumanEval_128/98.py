
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
    # if len(arr) == 0:
    #     return None
    # signs_multiplier = 1
    # for x in arr:
    #     if x == 0:
    #         signs_multiplier *= 0
    #     elif x > 0:
    #         signs_multiplier *= 1
    #     else:
    #         signs_multiplier *= -1
    # return sum([abs(x) for x in arr]) * signs_multiplier

    # Solution 2:
    # if len(arr) == 0:
    #     return None
    # signs_multiplier = 1
    # for x in arr:
    #     if x == 0:
    #         signs_multiplier = 0
    #         break
    #     elif x > 0:
    #         signs_multiplier *= 1
    #     else:
    #         signs_multiplier *= -1
    # return sum([abs(x) for x in arr]) * signs_multiplier

    # Solution 3:
    if len(arr) == 0:
        return None
    signs_multiplier = 1
    for x in arr:
        if x != 0:
            if x > 0:
                signs_multiplier *= 1
            else:
                signs_multiplier *= -1
            break
    return sum([abs(x) for x in arr]) * signs_multiplier

