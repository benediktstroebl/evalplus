
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
    # Your code here
    if(a % 10 == 0 and b % 10 == 0):
        return 0
    else:
        x = int(a)
        y = int(b)
        product = 0
        while x != 0:
            product = product*10 + (x % 10)
            x = (x // 10)
        while y != 0:
            product = product*10 + (y % 10)
            y = (y // 10)
        return product
