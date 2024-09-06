
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
    b = abs(b)
    a = abs(a)
    product = 0
    while a and b:
        digit_a, number_a = int(a % 10), a // 10
        digit_b, number_b = int(b % 10), b // 10
        product = product * 10 + digit_b * digit_a
        a, b = number_a, number_b
    negative = bool(a or b)
    negative = (negative) * -1
    return (negative, int(product))[0]
