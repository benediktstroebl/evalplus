
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
    num = a * b
    num_list = list(str(num))
    if num_list[0] == '-':
        num_list.pop(0)
    final = ''
    for i in num_list:
        final = final + i
    return int(final)

