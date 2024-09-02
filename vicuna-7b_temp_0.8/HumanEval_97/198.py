
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
    while True:
        c = sum(int(digit) * (9 ** (len(str(a)) - len(str(b)))) for digit in str(a) for str(b) in str(b))
        if c > 9:
            return "0" + str(c % 10)
        if c < 10:
            return "0" + str(c)
        a, b = b, a
