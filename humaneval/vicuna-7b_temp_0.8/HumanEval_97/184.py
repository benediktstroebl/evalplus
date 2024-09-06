
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
    # handle the special case when the last digit of the first number
    # is zero and the last digit of the second number is zero
    if a[-1] == 0 and b[-1] == 0:
        return 0
    # handle the special case when the second number is zero
    if b == 0:
        return 0
    # handle the special case when the first number is zero
    if a == 0:
        return 0
    # handle the special case when the last digit of the first number
    # is the same as the last digit of the product
    if a[-1] == b[-1]:
        return int(a[-1])
    # convert both numbers to strings
    a = str(a)
    b = str(b)
    # loop through the digits of the numbers
    carry = 0
    for i in range(len(a)-1, len(a)):
        # get the unit digit of the product
        unit_digit = int(b[i]) + int(a[i]) + carry
        # if the unit digit is greater than 9, the carry will be 1
        carry = (unit_digit - 9) // 10
        # update the product digit
        b = str(b[:i] + unit_digit + carry) + b[i+1:]
    # return the product as a string
    return b