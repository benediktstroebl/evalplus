def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(num) for num in arr) * product(num % 2 for num in arr)
    return result