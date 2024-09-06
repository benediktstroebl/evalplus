
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

    product = a * b
    unit_digit = 0
    digit = 0
    while product >= 10:
        product = product // 10
        digit += 1
    while unit_digit < product:
        unit_digit += 1
    while unit_digit > 0:
        unit_digit = unit_digit // 10
        digit -= 1
        if product >= unit_digit:
            product = product % unit_digit
    return digit

