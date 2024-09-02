
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
    a = str(a)
    b = str(b)
    prod = 0
    for i in range(len(a)):
        for j in range(len(b)):
            if a[-1-i] == b[-1-j]:
                prod += int(a[-1-i])*int(b[-1-j])
    return prod
