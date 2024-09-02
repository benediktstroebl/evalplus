
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
    if b < 0:
        return multiply(-a, abs(b))

    if a < 0:
        return multiply(-a, abs(b))

    if a == 0 or b == 0:
        return 0

    digits = [a, b]
    digits.sort()
    result = 0
    for i in range(2, len(digits) + 1, 2):
        result += digits[i - 2] * digits[i - 1] * digits[i]

    return result