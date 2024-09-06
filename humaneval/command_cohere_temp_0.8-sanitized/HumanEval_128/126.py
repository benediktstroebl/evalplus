def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign_product = arr_len - sum(1 for n in arr if n == 0)
        num_product = sum(abs(n) for n in arr)
        result = num_product * sign_product
    return result