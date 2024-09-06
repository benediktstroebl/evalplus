
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
    # Your code here
    prod = a * b

    # a = 111
    # b = 122

    a_digits = [int(x) for x in str(a)]
    b_digits = [int(x) for x in str(b)]

    # a_digits = [1, 1, 1]
    # b_digits = [1, 2, 2]

    a_unit_digit = a_digits[len(a_digits) - 1]
    b_unit_digit = b_digits[len(b_digits) - 1]

    return a_unit_digit * b_unit_digit
