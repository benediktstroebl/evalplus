
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
    # check if either of the number is negative
    if abs(a) > 9 or abs(b) > 9:
        return 0
    # check if the numbers are within the range of valid integers
    if a < 0 or a > 99 or b < 0 or b > 99:
        return 0
    # convert the number to base 10
    a_base10 = a // 10
    b_base10 = b // 10
    # check the leading digit of the unit's place
    if a_base10 == b_base10:
        return 0
    else:
        product = 0
        while a_base10 != 0:
            product = product * 10 + a_base10 % 10
            a_base10 //= 10
        while b_base10 != 0:
            product = product * 10 + b_base10 % 10
            b_base10 //= 10
        # convert the product back to decimal
        product = product * 10**(10-(a_base10+b_base10))
        return product
