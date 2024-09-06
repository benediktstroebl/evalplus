def prod_signs(arr):
    result = None
    if arr:
        arr_signs = [math.copysign(1, num) for num in arr]
        result = sum([abs(num) for num in arr]) * prod(arr_signs)
    return result
def prod(iterable):
    result = 1
    for x in iterable:
        result *= x
    return result