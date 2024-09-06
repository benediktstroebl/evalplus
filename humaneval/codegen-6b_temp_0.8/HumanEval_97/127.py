
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
    a = abs(a)
    b = abs(b)
    carry = 0
    prod = 0
    while (a > 0) or (b > 0): # pay attention to the while loop
        digit_a = a % 10
        digit_b = b % 10
        prod = digit_a * digit_b + carry
        carry = prod // 10
        prod = prod % 10
        a = a // 10
        b = b // 10
    if prod > 0:
        return prod
    else:
        return 10 + prod

"""