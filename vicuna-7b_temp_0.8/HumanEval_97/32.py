
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
    digit_a = str(a)
    digit_b = str(b)
    while len(digit_a) < len(digit_b):
        digit_a = "0" + digit_a
    while len(digit_b) < len(digit_a):
        digit_b = "0" + digit_b
    carry = 0
    product = 0
    for i in range(len(digit_a)):
        if digit_a[i] == digit_b[i]:
            product += product * 10
            carry += carry * 10
            if i == len(digit_a) - 1:
                if carry > 9:
                    carry = carry - 10
                    product = product * 10
                else:
                    product = product + "0"
        else:
            product = "0" + product
            carry = "0" + carry
    return product + carry
