
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
    ans = 1
    last_digit = 1
    while b > 0:
        if b % 10 == 0:
            b //= 10
            continue
        last_digit *= b % 10
        b //= 10
    if last_digit > 10:
        last_digit = last_digit % 10
    return last_digit
