def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        signs = [1 if i > 0 else -1 if i < 0 else 0 for i in arr]
        signs_product = functools.reduce(lambda x, y: x * y, signs, 1)
        magnitudes = [abs(i) for i in arr]
        magnitudes_sum = sum(magnitudes)
        result = magnitudes_sum * signs_product
    return result