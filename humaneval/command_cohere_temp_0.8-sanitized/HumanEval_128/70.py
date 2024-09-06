def prod_signs(arr):
    result = None
    if arr:
        arr = [x for x in arr if x != 0]
        signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
        result = sum([x * y for x, y in zip(arr, signs)])
    return result