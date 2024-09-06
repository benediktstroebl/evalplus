
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
    sign = 1
    if a < 0 and b < 0:
        sign = -1
    if a < 0:
        a *= -1
    if b < 0:
        b *= -1

    a *= 10
    b *= 10
    answer = 0
    while a or b:
        a_digit = a % 10
        b_digit = b % 10
        answer += a_digit * b_digit
        a //= 10
        b //= 10
    return sign * answer