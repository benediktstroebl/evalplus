
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
    #TODO: Your code here
    a_last = a % 10
    a_num = a // 10
    b_last = b % 10
    b_num = b // 10
    while a_num != 0 and b_num != 0:
        a_num = a_num % 10
        a_last = a_last * a_num
        b_num = b_num % 10
        b_last = b_last * b_num
        a_last = a_last % 10
        b_last = b_last % 10
    return a_last * b_last
