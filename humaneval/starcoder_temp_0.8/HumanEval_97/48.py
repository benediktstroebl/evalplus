
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
    a_list = []
    b_list = []
    for x in a:
        a_list.append(int(x))
    for y in b:
        b_list.append(int(y))
    result = 0
    for x in a_list:
        for y in b_list:
            result = result + x*y
    return result
