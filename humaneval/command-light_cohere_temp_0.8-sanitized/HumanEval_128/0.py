def prod_signs(arr):
    if not_enough_elements(arr):
        return None
    result = 1
    sign = 1
    for num in arr:
        result *= num
        result += sign
        sign *= -1
    return result
def not_enough_elements(arr):
    if not arr or len(arr) < 1:
        return False
    return True