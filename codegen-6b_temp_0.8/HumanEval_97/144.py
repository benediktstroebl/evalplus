
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
    if a == 0 or b == 0:
        return 0
    x = abs(a)
    y = abs(b)
    remaining_digits = []
    if x > y:
        remaining_digits = list(str(x))
        a_digits = list(str(x))
    else:
        remaining_digits = list(str(y))
        b_digits = list(str(y))
    new_digits = []
    carry = 0
    for i in range(len(remaining_digits)):
        if len(remaining_digits) == i:
            remaining = 0
        else:
            remaining = int(remaining_digits[i])
        if (len(remaining_digits) - i) > len(b_digits):
            b_digit = 0
        else:
            b_digit = int(b_digits[len(remaining_digits) - i - 1])
        new_digit = int((remaining * b_digit) + carry)
        carry = 1 if new_digit > 9 else 0
        new_digits.append(new_digit)
    new_digits_str = "".join(map(str, new_digits))
    if new_digits_str[0] == "-":
        new_digits_str = new_digits_str[1:]
    return int(new_digits_str)
    
