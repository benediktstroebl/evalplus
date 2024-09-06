
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

    if a <= 0:
        return 0
    if b <= 0:
        return 0
    if a == 1 or b == 1:
        return 1

    l = [int(x) for x in str(a)]
    m = [int(x) for x in str(b)]
    
    summ = 0
    for i in l:
        for j in m:
            summ += i*j

    return summ
    
