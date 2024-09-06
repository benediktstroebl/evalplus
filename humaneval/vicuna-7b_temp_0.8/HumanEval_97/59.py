
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
    # The function multiplies the two numbers and then converts each digit
    # to its corresponding unit digit and multiplies them.
    product = 0
    for i in range(10):
        digit_i = int(a / 10**i)
        digit_j = int(b / 10**i)
        if (digit_i, digit_j) not in product_list:
            product *= 10
            product_list.append((digit_i, digit_j))
        a, b = int(a) / 10**(i+1), int(b) / 10**(i+1)
        product = product * 10 + product_list[-1]
    return product
