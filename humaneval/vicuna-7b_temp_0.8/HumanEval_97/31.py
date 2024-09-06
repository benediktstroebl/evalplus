
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
    # Part 1: Parse the input strings
    a = int(a)
    b = int(b)
    # Part 2: Handle the cases where the product is 0
    if a == 0:
        return b
    elif b == 0:
        return 0
    elif a % 10 == b % 10:
        # Part 3: Convert the last digit of a and b to 1
        a_last_digit = a % 10
        b_last_digit = b % 10
        return int(str(a_last_digit) * str(b_last_digit))
    else:
        # Part 4: Convert the last digit of a and b to 1
        a_last_digit = str(a % 10)
        b_last_digit = str(b % 10)
        # Part 5: Multiply the digits of a and b
        product = 0
        for i, digit in enumerate(a_last_digit):
            product = product * 10 + int(digit) * (str(b_last_digit[i]) + str(str(b_last_digit)[i]))
        return int(product)