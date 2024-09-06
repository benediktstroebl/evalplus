
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
    # Write code here
    while True:
        c = a % 10
        a = a // 10
        d = b % 10
        b = b // 10
        if c == d:
            # If the units digit of both the numerator and denominator are the same, the product is 10
            return 10
        elif (c != d) or (a == 0 or b == 0):
            # If the units digit of the numerator is different from the denominator or the numerator or denominator is 0, the product is the units digit of the numerator multiplied by the units digit of the denominator
            return c * d
        else:
            return 0
