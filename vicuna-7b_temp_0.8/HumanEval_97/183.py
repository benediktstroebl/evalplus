
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
    #convert input numbers to string
    str_a = str(a)
    str_b = str(b)
    
    #convert unit digit of each number to a list
    str_a_unit = str_a[:-2]
    str_a_ones = str_a[-2:]
    str_b_unit = str_b[:-2]
    str_b_ones = str_b[-2:]
    
    #check if the number of ones is odd or even
    if str_a_unit[-1] == '1' and str_b_unit[-1] == '1':
        return '0'
    else:
        if int(str_a_unit[-1])*int(str_b_unit[-1]) % 10 == 0:
            return int(str_a_unit[-1])*int(str_b_unit[-1]) // 10
        else:
            return '0' + str(int(str_a_unit[-1])*int(str_b_unit[-1]) // 10)
            
