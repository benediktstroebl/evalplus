def prod_signs(arr):
    result = None
    if arr:
        signs = [1 if num > 0 else -1 if num < 0 else 0 for num in arr]
        result = sum(num * sign for num, sign in zip(arr, signs))
    return result