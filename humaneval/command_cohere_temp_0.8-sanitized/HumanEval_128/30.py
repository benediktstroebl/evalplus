def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        product_of_signs = functools.reduce(lambda x, y: x * y, signs, 1)
        result = sum(magnitudes) * product_of_signs
    return result