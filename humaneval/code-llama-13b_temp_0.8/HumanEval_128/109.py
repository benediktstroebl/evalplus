
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
    # O(n) time | O(n) space
    # import math
    # if len(arr) == 0:
    #     return None
    #
    # product = 1
    # for num in arr:
    #     product *= math.copysign(1, num)
    #
    # if product < 0:
    #     sum_mag_neg_abs = sum(abs(num) for num in arr if num < 0)
    #     return sum_mag_neg_abs
    #
    # return sum(abs(num) for num in arr if num > 0)

    # Solution 2
    # O(n) time | O(1) space
    if len(arr) == 0:
        return None

    sum_of_magnitudes = 0
    product_of_signs = 1
    for num in arr:
        sum_of_magnitudes += abs(num)
        product_of_signs *= 1 if num == 0 else num / abs(num)
    return sum_of_magnitudes * product_of_signs

