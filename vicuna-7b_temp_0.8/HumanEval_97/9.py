
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
    a, b = map(int, [a, b])
    if (a/10) == (b/10):
        return a*b
    else:
        l = str(a)
        r = str(b)
        while l or r:
            if l[0] == r[0]:
                l = l[1] + l[1]
                r = r[1] + r[1]
            else:
                if l[0] < r[0]:
                    l = l[1] + l[1]
                    r = r[1] + r[1] + "0"
                else:
                    l = l[1] + l[1]
                    r = r[1] + r[1] + "0"
        return int(l) * int(r)