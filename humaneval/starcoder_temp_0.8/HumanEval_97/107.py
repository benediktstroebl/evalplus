
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
    a,b = abs(a), abs(b)
    a = a % 100
    b = b % 100
    summ = 0
    for i in range(0,100):
        summ += ((a // 10**(9-i)) % 10) * ((b // 10**(9-i)) % 10)
    return summ % 100
