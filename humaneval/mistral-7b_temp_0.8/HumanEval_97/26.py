
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
    num1 = str(a)
    num2 = str(b)
    num1_unit = num1[-1]
    num2_unit = num2[-1]
    unit_digit = int(num1_unit)*int(num2_unit)
    return unit_digit
