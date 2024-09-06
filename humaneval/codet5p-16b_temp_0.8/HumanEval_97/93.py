
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

    if a.isnumeric() == False or b.isnumeric() == False:
        return None

    if len(a) > 1 and len(b) > 1:
        return None

    if len(a) == 1 and len(b) == 1:
        return None

    if len(a) == 0:
        a = '0'
    if len(b) == 0:
        b = '0'

    a = a.strip()
    b = b.strip()

    a = a.split('0')
    b = b.split('0')

    x = a[0]
    y = b[0]

    return int(x) * int(y)

