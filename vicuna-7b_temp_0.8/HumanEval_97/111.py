
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
    while True:
        if b >= 100:
            d = 0
            for i in range(b // 100, -1, -1):
                d = d * 100 + i
                b = b - 100 * i
            if a % 100 == d:
                return a * 100 + d
        elif b >= 10:
            d = 0
            for i in range(b // 10, -1, -1):
                d = d * 10 + i
                b = b - 10 * i
            if a % 10 == d:
                return a * 10 + d
        elif b == 0:
            return 0
        else:
            if a >= 10:
                e = 0
                for i in range(a // 10, -1, -1):
                    e = e * 10 + i
                    a = a - 10 * i
                if b == e:
                    return a * 10 + e
            elif a >= 1:
                f = 0
                for i in range(a // 1, -1, -1):
                    f = f * 10 + i
                    a = a - 10 * i
                if b == f:
                    return a * 10 + f
            else:
                return 0
    
    
