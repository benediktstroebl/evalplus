
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
    #print('bonus multiply')
    #print('a',a,'b',b)
    if a < 0:
        b = -b
        a = -a
    if b >= 10:
        a, b = b, a
    a_str = str(a)
    b_str = str(b)
    
    
    a_digits = []
    for i in range(len(a_str)):
        a_digits.append(int(a_str[-(i+1)]))
        
    b_digits = []
    for i in range(len(b_str)):
        b_digits.append(int(b_str[-(i+1)]))
    
    len_a = len(a_digits)
    len_b = len(b_digits)
    
    
    product = [0 for _ in range(len_a + len_b)]
    p_i = 0
    for i in range(len(a_digits)):
        p_i = 0
        for j in range(len(b_digits)):
            p_i += a_digits[i] * b_digits[j]
        product[i + j] = p_i
    
    #print('product',product)
    return reduce(lambda x,y: x * 10 + y, product[::-1])
