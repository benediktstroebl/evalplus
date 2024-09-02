
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

    a_s = str(a)
    b_s = str(b)

    a_s_numbers = []
    b_s_numbers = []

    for i in a_s:
        a_s_numbers.append(i)
    
    for i in b_s:
        b_s_numbers.append(i)

    a_s_int = []
    b_s_int = []

    for i in a_s_numbers:
        a_s_int.append(int(i))
    
    for i in b_s_numbers:
        b_s_int.append(int(i))

    a_s_sum = 0
    b_s_sum = 0

    for i in a_s_int:
        a_s_sum += i

    for i in b_s_int:
        b_s_sum += i

    return a_s_sum * b_s_sum
