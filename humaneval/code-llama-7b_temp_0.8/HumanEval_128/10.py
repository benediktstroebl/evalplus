
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
    if not arr:
        return None

    sign = 1
    arr_sum = 0
    arr_prod = 1
    for i in arr:
        if sign == 1:
            if i == 0:
                sign = 0
            elif i > 0:
                arr_sum += i
            else:
                arr_sum += i
                sign = -1
        elif sign == -1:
            if i == 0:
                sign = 0
            elif i > 0:
                arr_sum += i
                sign = 1
            else:
                arr_sum += i
                sign = 1
                arr_prod *= -1
        else:
            if i == 0:
                return 0
            else:
                return None
        arr_prod *= i
    return arr_sum * arr_prod

