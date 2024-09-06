def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x%3 for x in arr)
    return result