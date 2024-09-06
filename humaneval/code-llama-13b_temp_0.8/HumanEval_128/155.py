
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
    # O(n) time, O(1) space
    # n = len(arr)
    # signs = 1
    # for x in arr:
    #     if x > 0:
    #         signs *= 1
    #     elif x < 0:
    #         signs *= -1
    #     else:
    #         signs *= 0
    # prod = 1
    # for x in arr:
    #     prod *= x
    # return prod * signs

    # Solution 2
    # O(n) time, O(n) space
    signs = [1 if x else 0 for x in arr]
    for i in range(1, len(arr)):
        signs[i] *= signs[i - 1]
    signs = [1] + signs[:-1]
    signs[0] = 1

    prod = 1
    for i, x in enumerate(arr):
        prod *= x * signs[i]

    return prod

