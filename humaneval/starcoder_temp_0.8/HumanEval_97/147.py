
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
    a_string = str(a)
    b_string = str(b)
    product = 0
    for i in range(len(a_string)):
        product += int(a_string[i]) * int(b_string[i])
    return product
