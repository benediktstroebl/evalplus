
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
    product = 0
    for num1 in range(len(a)):
        num1 = int(a[num1])
        for num2 in range(len(b)):
            num2 = int(b[num2])
            product += (num1 * num2)
    return product
    
