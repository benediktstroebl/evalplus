
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
    x = abs(a)
    y = abs(b)
    ans = 0
    while x:
        x, digit = divmod(x, 10)
        ans += digit * (y % 10)
    return 0 if ans < 0 else ans
