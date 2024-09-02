
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
    if b < 0:
        b = -b
    if b > a:
        a, b = b, a
    a_int = a
    a_str = str(a)
    b_int = b
    b_str = str(b)
    prod_str = ''
    for i in a_str:
        if i == '0':
            prod_str += i
        else:
            num_i = int(i)
            for j in b_str:
                if j == '0':
                    continue
                else:
                    num_j = int(j)
                    prod_num = num_i * num_j
                    prod_str += str(prod_num)[-1]
    prod = int(prod_str)
    if prod >= 10:
        return multiply(prod, b_int)
    else:
        return prod
