
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
    mult = 1
    if a == -1:
        return (-1)*b
    if b == -1:
        return (-1)*a
    for i in range(abs(a)):
        mult *= abs(b)
    if (a > 0) and (b < 0):
        return mult*-1
    if (a > 0) and (b > 0):
        return mult
    if (a < 0) and (b > 0):
        return mult*-1
    if (a < 0) and (b < 0):
        return -(mult)

assert multiply(148, 412) == 16
assert multiply(19, 28) == 72
assert multiply(2020, 1851) == 0
assert multiply(14,-15) == 20
