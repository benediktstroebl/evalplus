
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

    if a < 0: a = -a
    if b < 0: b = -b

    ans = a
    for i in range(1, len(str(b))):
        ans = ans * 10
        ans += a % 10
        a //= 10

    return ans


