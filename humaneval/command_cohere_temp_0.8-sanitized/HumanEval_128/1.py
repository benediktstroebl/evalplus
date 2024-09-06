def prod_signs(arr):
    result = None
    if arr:
        arr = [x for x in arr if x]
        product = 1
        for x in arr:
            product *= x
        result = abs(product)
    return result