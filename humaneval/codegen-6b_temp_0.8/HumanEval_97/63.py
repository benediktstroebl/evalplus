
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
    m, n = abs(a), abs(b)
    result = 0
    while m > 0:
        result += n
        m, n = m - (m/10)*10, m%10
    return -result if a < 0 and b < 0 else result

