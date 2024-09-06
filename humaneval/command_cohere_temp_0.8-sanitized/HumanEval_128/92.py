def prod_signs(arr):
    result = None
    if arr:
        arr = [abs(x) for x in arr]
        arr = [x * y for x, y in zip(arr, [1, -1])]
        result = sum(arr)
    return result