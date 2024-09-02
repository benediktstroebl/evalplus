
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
    # Get the last digits of a and b
    a_last_digit = str(a)[-1]
    b_last_digit = str(b)[-1]
    # Make the last digits of a and b the first digits of the product
    product_last_digit = a_last_digit * b_last_digit
    # Put the remaining digits of a and b in the right place to get the final product
    product_digits = []
    for i in range(len(a_last_digit)):
        product_digits.append(str(a)[i:i+1])
        product_digits.append(str(b)[i+1:])
    # Join the product_digits together to get the final product
    product = ''.join(product_digits)
    return product