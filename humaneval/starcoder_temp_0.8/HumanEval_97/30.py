
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
    #YOUR CODE GOES HERE
    if len(str(a)) == 1 or len(str(b)) == 1:
        return 0
    a_list = list(str(a))
    b_list = list(str(b))
    a_list.sort()
    b_list.sort()
    if a_list[0] == '0' or b_list[0] == '0':
        return 0
    mul_list = []
    for a_item in a_list:
        for b_item in b_list:
            if int(a_item)*int(b_item) < 10:
                mul_list.append(int(a_item)*int(b_item))
    if len(mul_list) == 0:
        return 0
    else:
        return int(''.join([str(int) for int in mul_list]))
