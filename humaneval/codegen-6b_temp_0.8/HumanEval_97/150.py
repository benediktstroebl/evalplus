
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
    carry = 0
    product = 0
    while b != 0:
        digit = b % 10
        carry = (a * digit + carry) // 10
        product = (product * 10) + carry
        b = b // 10
    return product
