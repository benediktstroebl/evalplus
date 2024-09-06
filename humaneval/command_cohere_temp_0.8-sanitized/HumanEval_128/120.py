def prod_signs(arr):
    result = None
    if arr:
        arr = [x * s for x, s in enumerate(arr, 1)]
        result = sum(x for x in arr if x)
    return result