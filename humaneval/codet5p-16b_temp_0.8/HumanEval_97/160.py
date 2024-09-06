
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
    elif a < 0 or b < 0:
        return -multiply(-a, -b)
    else:
        a_lst = [int(i) for i in list(str(a))]
        b_lst = [int(i) for i in list(str(b))]
        a_multiply_b_lst = [a * b for a, b in zip(a_lst, b_lst)]
        return int("".join(str(i) for i in a_multiply_b_lst))
        
