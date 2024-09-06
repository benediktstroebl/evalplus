def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign_prod = arr_len - sum(x % 2 for x in arr)
        num_mag = sum(x for x in arr if x)
        result = num_mag * sign_prod
    return result