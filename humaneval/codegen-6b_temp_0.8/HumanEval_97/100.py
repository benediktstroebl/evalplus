
def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """
    result_digits = []
    for digit_a, digit_b in zip(str(a), str(b)):
        result_digits.append(int(str(digit_a) + str(digit_b)))
    result = reduce(lambda x, y: x * y, result_digits)
    return result

assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14,-15) == 20
assert multiply(100,-999) == 0
assert multiply(0,0) == 0
assert multiply(-913, -457) == 0