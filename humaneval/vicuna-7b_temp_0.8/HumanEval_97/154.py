
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
    # 5. Convert the input numbers to base 10.
    a_in_base10 = str(a)
    b_in_base10 = str(b)
    # 6. Extract the units digits of a and b.
    a_units_digits = map(int, a_in_base10.split())
    b_units_digits = map(int, b_in_base10.split())
    # 7. Append the units digits of a and b.
    a_product = 0
    b_product = 0
    for i in range(len(a_units_digits)):
        a_product = a_product * 10 + a_units_digits[i]
        b_product = b_product * 10 + b_units_digits[i]
    # 8. Add the remaining digits of a and b.
    a_product = a_product * 10 + (b_units_digits[len(a_units_digits)] if len(a_units_digits) > 0 else 0)
    b_product = b_product * 10 + (a_units_digits[len(a_units_digits)] if len(a_units_digits) > 0 else 0)
    # 9. Append zeros to the product to make it the same length as the shorter input number.
    if len(a_product) > len(b_product):
        a_product = a_product + '0'*(len(b_product)-len(a_product))
    elif len(a_product) < len(b_product):
        b_product = b_product + '0'*(len(a_product)-len(b_product))
    # 10. If the product is negative, reverse it.
    if a_product[0] < 0:
        a_product = '-' + a_product[1:]
    return a_product
