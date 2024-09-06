def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1)
        signs *= [num < 0 for num in arr]
        result = sum([num for num in arr]) * prod(signs)
    return result