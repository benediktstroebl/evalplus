def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result