
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
    result = 0
    if not arr:
        return None
    sign_mul = 1
    for num in arr:
        if not num:
            sign_mul = 0
        else:
            sign_mul *= num / abs(num)
        result += abs(num) * sign_mul
    return result
    # Solution 2
    # sign_mul = -1 if 0 in arr else 1 if all(x > 0 for x in arr) else 0
    # return sum(abs(num) * sign_mul for num in arr)
