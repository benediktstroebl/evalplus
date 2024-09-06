
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
    result = 0
    for index in range(max(len(str(a)), len(str(b)))):
        digit = (a // 10**(index)) % 10
        carry += digit * (b // 10**(index)) % 10
        result += digit * (b // 10**(index))
    return result + carry

