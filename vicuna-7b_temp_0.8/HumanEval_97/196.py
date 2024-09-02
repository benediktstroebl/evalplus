
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
    # return 0 if either input is 0
    if a == 0 or b == 0:
        return 0
    # reverse the digits of each input
    a = str(int(a))[::-1]
    b = str(int(b))[::-1]
    # copy the digits from the end of the shorter input to the beginning
    result = ""
    while a or b:
        if a:
            result += a[-1]
        if b:
            result += b[-1]
        a = int(a[:-1])
        b = int(b[:-1])
    # reverse the digits of the result
    result = str(int(result))[::-1]
    return result
