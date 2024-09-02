
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

    product = a * b
    product = str(product)
    new_product = ''
    for index, digit in enumerate(product):
        if digit.isdigit() == True:
            if index == 0 and int(digit)!= 0:
                new_product += str(int(digit) * a)
            if index == 1 and int(digit)!= 0:
                new_product += str(int(digit) * b)
    return int(new_product)
