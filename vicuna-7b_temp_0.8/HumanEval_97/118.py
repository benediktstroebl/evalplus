
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
    # divide by 10 repeatedly
    while a != 0:
        a = a // 10
        b = b // 10
        if a < b:
            return 0
        if a > b:
            return 10 * _multiply(b, a - b)
    return 0
