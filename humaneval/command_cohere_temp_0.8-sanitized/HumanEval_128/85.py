def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1)
        signs *= arr[0]
        result = sum([num for num in arr if num]) * signs
    return result