
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
    print(f'A is {a}')
    print(f'B is {b}')
    
    str_a = str(a)
    str_b = str(b)
    
    if len(str_a) > 1:
        a_unit = int(str_a[-1])
    else:
        a_unit = int(str_a)
        
    if len(str_b) > 1:
        b_unit = int(str_b[-1])
    else:
        b_unit = int(str_b)
    
    return a_unit * b_unit
    
    
