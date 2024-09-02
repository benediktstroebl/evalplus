
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
        while a > 9:
            a, remainder = a//10, a%10
            b, remainder = b//10, b%10
            if remainder > 9:
                break
        while b > 9:
            b, remainder = b//10, b%10
            if remainder > 9:
                break
        product = 0
        while a >= 10 and b >= 10:
            product = (product * 10) + (a % 10 * b % 10)
            a, remainder = a//10, a%10
            b, remainder = b//10, b%10
            if remainder > 9:
                break
        if remainder > 9:
            product = product * 10 + (remainder * 10)
        return product