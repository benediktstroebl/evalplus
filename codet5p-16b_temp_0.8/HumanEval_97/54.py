
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

    if a <= 0 or b <= 0:
        return 0
    else:
        product = 0
        a_str = str(a)
        b_str = str(b)
        a_int = int(a_str)
        b_int = int(b_str)
        for i in str(a_int):
            product += int(i)
        for i in str(b_int):
            product += int(i)
        return product
