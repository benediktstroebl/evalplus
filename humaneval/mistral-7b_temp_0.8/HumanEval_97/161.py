
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
    a=str(a)
    b=str(b)
    a_num=a[-1]
    b_num=b[-1]
    if a_num=='0' or b_num=='0':
        return 0
    else:
        return int(a_num)*int(b_num)
