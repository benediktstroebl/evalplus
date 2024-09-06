def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign = 1
        for x in arr:
            sign *= x
            if sign == 0:
                sign = 1
        result = sum(abs(x) for x in arr) * sign
    return result