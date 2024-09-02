
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
    # get the product in str
    product = str(int(a) * int(b))
    # get the product as a list
    product = list(product)
    # divide the product by 10 everytime to get the unit digits
    for i in range(len(product)):
        product[i] = int(product[i]) / 10
    return sum(product)
