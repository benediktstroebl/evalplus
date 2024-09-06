
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
    a = int(a)
    b = int(b)
    d = []
    res = 0
    for digit in str(a):
        d.append(int(digit))
    for digit in str(b):
        d.append(int(digit))
    d.sort(reverse = True)
    for i in d:
        res += i
    return res

