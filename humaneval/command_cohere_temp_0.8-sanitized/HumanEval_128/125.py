def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(num) for num in arr) * product(sign(num) for num in arr)
    return result
def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0