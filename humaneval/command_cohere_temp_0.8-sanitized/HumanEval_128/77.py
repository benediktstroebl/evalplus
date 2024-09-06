def prod_signs(arr):
    result = None
    if arr:
        signs = [x > 0 for x in arr] * [x < 0 for x in arr] + [x == 0 for x in arr]
        result = sum(x * y for x, y in zip(arr, signs))
    return result