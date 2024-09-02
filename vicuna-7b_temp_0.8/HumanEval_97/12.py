
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
    # check if the input is negative
    if b < 0:
        # convert the input to a string and subtract the integer part
        b = str(b) + "0"*(len(str(b))-len(str(abs(b))))
        return multiply(int(a), b)
    elif a < 0:
        return multiply(int(b), -a)
    else:
        # convert the input to a string and sum the unit digits
        a_str = str(a)
        b_str = str(b)
        if a_str[-1] == "0":
            a_str = a_str[:-1]
        if b_str[-1] == "0":
            b_str = b_str[:-1]
        a_unit_digits = [int(digit) for digit in a_str]
        b_unit_digits = [int(digit) for digit in b_str]
        product = []
        for i in range(len(a_unit_digits)):
            for j in range(len(b_unit_digits)):
                product.append(0)
                result = 0
                for k in range(len(a_unit_digits)):
                    for l in range(len(b_unit_digits)):
                        result += a_unit_digits[k] * b_unit_digits[l] // 10
                product.append(result)
        if a_unit_digits[-1] == "1":
            product.append(1)
        return ".".join(map(str, product))
