
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
    for i in range(b):
        digit = a & 1
        a = a >> 1
        if carry:
            a = a | ~0
            carry = carry >> 1
        result = result | digit
    return result
