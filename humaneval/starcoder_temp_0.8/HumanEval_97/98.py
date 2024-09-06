
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
    a_1 = a % 10
    a_2 = (a // 10) % 10
    a_3 = (a // 100) % 10
    a_4 = (a // 1000) % 10

    b_1 = b % 10
    b_2 = (b // 10) % 10
    b_3 = (b // 100) % 10
    b_4 = (b // 1000) % 10

    return (a_1 * b_1 + a_2 * b_2 + a_3 * b_3 + a_4 * b_4)
