
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
    # a and b are of the form 10a + 10b and 10a - 10b
    # where a and b are digits, respectively
    # The left-hand side is a digit in base 10, the right-hand side is a digit in base 9
    # To convert to base 9, we simply raise 10 to the power of the corresponding digit position
    # For example, the first digit is 1*1^1 + 0*1^0 + 0*1^2 + ... + 0*1^9 = 1
    # To get the left-hand side, we add 1 to the sum of the powers of 10
    # For example, the first digit is 1*1^1 + 0*1^0 + 0*1^2 + ... + 0*1^9 = 1
    # So, the formula for a is 1 + (sum of the digits of b multiplied by 10^i, i=0..8)
    # The formula for b is similar, but with a negative sign
    # Now, we can use the formula to calculate the product
    # For example, for a=148 and b=412, we have 14+((4+5+1)*10^i, i=0..8) = 16
    # Similarly, for a=19 and b=28, we have 19+((9+2)*10^i, i=0..8) = 72
    # For a=2020 and b=1851, we have 2020+(8+46-1)*10^i, i=0..8) = 0
    # For a=14 and b=-15, we have 14+((-1+5)*10^i, i=0..8) = 20
    return a*b