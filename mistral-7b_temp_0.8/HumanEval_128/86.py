
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
    sign_prod = 1
    sign_count = 0
    sign_sum = 0
    for num in arr:
        if num != 0:
            sign_prod *= num
            sign_sum += num
        else:
            sign_sum = 0
        if num > 0:
            sign_count += 1
        elif num < 0:
            sign_count -= 1
    return sign_sum if sign_count == 0 else sign_prod if sign_count > 0 else -sign_prod

