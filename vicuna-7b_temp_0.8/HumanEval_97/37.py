
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
    # Step 1: Get the unit digits of both numbers
    a_unit_digit = get_unit_digit(a)
    b_unit_digit = get_unit_digit(b)
    
    # Step 2: If the two unit digits are the same, the product is 10 times the other digit.
    if a_unit_digit == b_unit_digit:
        b_digit = str(b_unit_digit)
        product = b_digit * 10 + str(b_unit_digit)
    # Step 3: Otherwise, the product is the sum of the unit digits.
    else:
        a_temp = str(int(a_unit_digit) * 10)
        b_temp = str(int(b_unit_digit) * 10)
        product = str(int(a_unit_digit) * int(b_unit_digit))
        if a_temp[-1] == '0' or b_temp[-1] == '0':
            product = product[:-1]
    
    return product
