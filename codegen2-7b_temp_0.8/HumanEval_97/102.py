
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
    a_length = len(str(a))
    b_length = len(str(b))
    result = 0
    for i in range(a_length):
        result += a % 10 * b % 10 * (10 ** (a_length - 1 - i))
        a //= 10
    for i in range(b_length):
        result += b % 10 * a % 10 * (10 ** (b_length - 1 - i))
        b //=
