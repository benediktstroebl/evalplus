
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
    a = abs(a)
    b = abs(b)
    _, a_, b_ = convert(a, b)
    c = 0
    start = 1
    while a_ > 0 and b_ > 0:
        if a_ & 1:
            c += b_
        if b_ & 1:
            c += a_
        a_ = a_ >> 1
        b_ = b_ >> 1
    if b < 0:
        c = -c + 1
    # if b is 0, c should be a%10
    if b == 0:
        c = a%10
    # if a is 0, c should be -b%10
    if a == 0:
        c = -b%10
    if c == 0:
        c = 1
    return c

