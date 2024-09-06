
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
    assert(0 <= a <= 9) and (0 <= b <= 9)
    if a == 0:
        return b + str(int(b))
    if b == 0:
        return a + str(int(a))
    if str(a) == str(b):
        return int(str(a) + str(b))
    else:
        unit_digits = []
        while True:
            carry = 0
            product = int(str(a)) * int(str(b))
            digit = product // 10
            product = product % 10
            a = str(a)[:-1]
            b = str(b)[:-1]
            if str(a) == str(digit):
                unit_digits.append(digit)
                carry += 1
            else:
                unit_digits.append(str(digit))
                carry = 0
            if str(b) == str(digit):
                unit_digits.append(digit)
                carry += 1
            else:
                unit_digits.append(str(digit))
            if carry > 9:
                break
        return (unit_digits[0] + str(carry)) + str(int(carry))
