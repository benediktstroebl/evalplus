def prod_signs(arr):
    result = None
    if arr:
        arr_signs = [num // abs(num) for num in arr]
        result = sum(num * sign for num, sign in zip(arr, arr_signs) if sign)
    return result