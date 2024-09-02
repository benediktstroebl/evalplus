
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
    a_digits = str(a).split("")
    b_digits = str(b).split("")
    a_unit = a_digits[-1]
    b_unit = b_digits[-1]
    result = ""
    for i in range(len(a_digits)-1):
        result = result + str(a_digits[i]) + str(b_digits[i])
        if a_digits[i] == b_digits[i] and a_digits[i] != a_unit and b_digits[i] != b_unit:
            result = result + "*"
        else:
            result = result + str(a_digits[i]) + str(b_digits[i])
    if a_unit == b_unit:
        result = result + str(a_unit)
    else:
        result = result + b_unit
    return int(result)
