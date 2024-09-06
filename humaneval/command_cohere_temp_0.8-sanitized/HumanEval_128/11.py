def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * arr[0]
        magnitudes = [abs(num) for num in arr]
        result = sum(magnitudes) * product(signs)
    return result