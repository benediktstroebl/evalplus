
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
    
    if a < 0:
        a = -a
    elif a == 0:
        return 0
        
    if b < 0:
        b = -b
    elif b == 0:
        return 0
        
    #split into digits
    a_list = list(str(a))
    b_list = list(str(b))
    
    #multiply digits
    result_list = [None] * (len(a_list)+len(b_list))
    result_index = len(result_list)-1
    
    a_index = len(a_list)-1
    b_index = len(b_list)-1
    
    while len(result_list) - 1 > result_index:
        
        if result_index >= 0:
            result_list[result_index] = int(a_list[a_index])*int(b_list[b_index])
            a_index-=1
            b_index-=1
            result_index-=1
        else:
            break
    
    a_index = len(a_list)-1
    b_index = len(b_list)-1
    
    while len(result_list) - 1 > result_index:
        
        if result_index >= 0:
            result_list[result_index] = int(a_list[a_index])*int(b_list[b_index])
            a_index-=1
            result_index-=1
        else:
            break
    
    result = int(''.join(str(e) for e in result_list))
    
    return result
