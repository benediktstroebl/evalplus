
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
    # check if either number is zero
    if a == 0 or b == 0:
        return 0
    
    # extract the unit digits
    ud_a = str(a)[1:]
    ud_b = str(b)[1:]
    
    # check if the units digit is the same
    if ud_a[-1] == ud_b[-1]:
        return int(ud_a[-1])
    else:
        # subtract the products of the first digits
        prod = abs(int(ud_a[0]) * int(ud_b[0]) - int(ud_b[0]) * int(ud_a[0]))
        return int(str(a)[1:]+str(b)[1:]) + prod
