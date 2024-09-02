
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
    arr_len = len(arr)
    if arr_len == 0:
        return None

    sign_dict = {}
    for i in range(arr_len):
        sign = arr[i]
        if sign == 1:
            sign_dict[i] = 1
        elif sign == -1:
            sign_dict[i] = -1
        else:
            sign_dict[i] = 0

    sign_dict_rev = dict(sign_dict)
    sign_dict_rev[len(arr_list)] = -sign_dict_rev[len(arr_list)]

    product = 1
    for i in range(arr_len):
        sign = sign_dict[i]
        if sign == 1:
            product *= arr_list[i]
        elif sign == -1:
            product *= -arr_list[i]
        else:
            product *= 0

    result = 0
    for i in range(arr_len):
        if sign_dict_rev[i] == -1:
            result *= arr_list[i] * product
        else:
            result *= product
    return result
