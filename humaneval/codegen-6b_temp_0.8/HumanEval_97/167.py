
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
    if a == 0 or b == 0:
        return 0
    a_digits = []
    while a>0:
        a_digits.append(a%10)
        a //= 10
    b_digits = []
    while b>0:
        b_digits.append(b%10)
        b //= 10
    product = 1
    for i in range(1, len(a_digits)+1):
        product *= a_digits[i-1]
    for i in range(1, len(b_digits)+1):
        product *= b_digits[i-1]
    return product
