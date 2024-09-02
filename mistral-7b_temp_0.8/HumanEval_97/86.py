
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
    # returns the unit digit
    def unit_digit(n):
        return n % 10

    # returns the first digit
    def first_digit(n):
        return n // 10

    return unit_digit(first_digit(a)) * unit_digit(first_digit(b))
