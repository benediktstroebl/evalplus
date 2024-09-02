
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
    # Normalize the input so the digits are in the range 0-9.
    a = str(a)
    b = str(b)
    a = [int(digit) for digit in a]
    b = [int(digit) for digit in b]
    c = [0] * 10
    d = [0] * 10
    for i in range(len(a)):
        c[a[i] - 1] += a[i]
        d[b[i] - 1] += b[i]
    result = 0
    while c:
        if c[0] > d[0]:
            result += d[0] - c[0]
        c.pop(0)
        d.pop(0)
    while c:
        i = c[0] % 10
        result += i + d[0] // 10
        c.pop(0)
        d.pop(0)
    return result // 100 * 100 + result % 100
