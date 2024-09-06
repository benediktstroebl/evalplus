
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
    if a > 0 and b > 0:
        a_list = [int(i) for i in str(a)]
        b_list = [int(i) for i in str(b)]
        a_list_sum = sum(a_list)
        b_list_sum = sum(b_list)
        return a_list_sum * b_list_sum
    else:
        return 0
