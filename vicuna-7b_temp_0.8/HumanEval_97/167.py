
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
    # Check that a and b are positive
    if b > 0:
        # Check that a is not zero
        if a != 0:
            return sum(int(d) * int(str(abs(b))[1:]) for d in str(a)[1:])
    elif a > 0:
        # Handle the case when b is zero
        return sum(int(d) * int(str(abs(a))[1:]) for d in str(b)[1:])
    else:
        return sum(int(d) * int(str(abs(b))[1:]) for d in str(a)[1:])
