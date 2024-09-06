def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * [-1, 1, 0]
        result = sum(abs(num) for num in arr) * signs.prod()
    return result