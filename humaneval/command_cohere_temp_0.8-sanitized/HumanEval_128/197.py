def prod_signs(arr):
    result = None
    if arr:
        signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        result = sum(abs(num) * sign for num, sign in zip(arr, signs))
    return result