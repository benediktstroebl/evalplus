
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
    result = 0
    a, b = abs(a), abs(b)

    # 'while' loop to iterate the number of times
    while a != 0 or b != 0:
        if a % 10 > b % 10:
            result += a % 10 * b % 10
            a = a // 10
        else:
            result += a % 10 * b % 10
            b = b // 10
    return result

