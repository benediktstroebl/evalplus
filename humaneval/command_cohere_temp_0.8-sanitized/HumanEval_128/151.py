def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign = 1
        for x in arr:
            sign *= x
        result = sum(x for x in arr if x != 0) * abs(sign)
    return result