
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
    a = str(a)
    b = str(b)
    product = 0
    for i in range(len(a)):
        if a[i] == '1':
            product = product * 10 + (b[i] - '1') * 10
        elif a[i] == '0':
            if b[i] == '1':
                product = product + 1
            else:
                product = product * 10
        else:
            product = product * 10 + (b[i] - '0') * 10
    return product