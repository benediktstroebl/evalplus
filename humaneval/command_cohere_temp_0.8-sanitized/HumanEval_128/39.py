def prod_signs(arr):
    result = None
    if arr:
        arr_signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        result = sum([abs(i) for i in arr]) * prod(arr_signs)
    return result