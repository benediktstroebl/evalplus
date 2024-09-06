
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

    # solution 1
    a = str(a)
    b = str(b)
    a = a[-1]
    b = b[-1]
    print(int(a)*int(b))
    return int(a)*int(b)


    # solution 2
    return int(str(a)[-1])*int(str(b)[-1])


    # solution 3
    return a % 10 * b % 10

