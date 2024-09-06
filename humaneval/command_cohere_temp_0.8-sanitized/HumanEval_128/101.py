def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        product_of_signs = prod(signs)
        result = sum(magnitudes) * product_of_signs
    return result