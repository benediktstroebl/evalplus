
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
    a = abs(a)
    b = abs(b)
    for i in range(0, len(str(a))):
        if a%10!= 0:
            if b%10!= 0:
                result += int(str(a)[i])*int(str(b)[i])
            else:
                return 0
        else:
            result += int(str(a)[i])
    for i in range(0, len(str(b))):
        if b%10!= 0:
            result += int(str(b)[i])
        else:
            return 0
    return result
