
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
    if arr == []:
        return None
    result = 0
    pos_arr = []
    neg_arr = []
    zero_arr = []
    for i in arr:
        if i > 0:
            result += i
            pos_arr.append(i)
        elif i < 0:
            result -= i
            neg_arr.append(i)
        else:
            result += i
            zero_arr.append(i)
    return result
    """
    """
    if arr == []:
        return None
    arr = list(arr)
    prod = 1
    result = 0
    for i in arr:
        if i > 0:
            result += i
            prod *= i
        elif i < 0:
            result -= i
            prod *= i
        elif i == 0:
            pass
    return prod
    """
