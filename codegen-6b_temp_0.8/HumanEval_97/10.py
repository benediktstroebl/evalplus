
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
    na = abs(a)
    nb = abs(b)
    # check if a is the least significant digit
    if a < 0:
        na = -na
    # check if b is the least significant digit
    if b < 0:
        nb = -nb
    for i in range(na):
        carry = carry + a % 10 * b % 10 * 10 ** (na - 1 - i)
        product = product + carry % 10 * 10 ** (na - 1 - i)
        carry = carry // 10
    product = product + carry
    
    if product < 0:
        product = product * -1
    elif product > 9:
        product %= 10

    return product

