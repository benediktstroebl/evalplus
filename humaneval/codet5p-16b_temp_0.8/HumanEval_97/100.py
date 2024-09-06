
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

    result = 0
    if a < 0 or b < 0:
        return result
    if len(str(a)) < 2 or len(str(b)) < 2:
        return result
    if len(str(a)) == 2 and len(str(b)) == 2:
        result += int(str(a)[0]) * int(str(b)[0])
        result += int(str(a)[1]) * int(str(b)[1])
        return result
    a_unit = int(str(a)[0])
    b_unit = int(str(b)[0])
    if a_unit == 0 or b_unit == 0:
        return result
    result += a_unit * b_unit
    result += multiply(int(str(a)[1]), int(str(b)[1]))
    return result

