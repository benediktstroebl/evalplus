
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

    num_a = a
    num_b = b
    result = 0
    if a > 0:
        while num_a > 0:
            remainder = num_a % 10
            num_a = num_a // 10
            result = result + remainder
    else:
        num_a = -num_a
    if b > 0:
        while num_b > 0:
            remainder = num_b % 10
            num_b = num_b // 10
            result = result + remainder
    else:
        num_b = -num_b
    return result

