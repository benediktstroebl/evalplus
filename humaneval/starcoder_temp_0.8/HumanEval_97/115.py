
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
    assert isinstance(a, int), "a must be an integer"
    assert isinstance(b, int), "b must be an integer"
    assert a >= 0, "a must be a positive integer"
    assert b >= 0, "b must be a positive integer"
    return int(''.join([str(int(i)*int(j)) for i,j in zip(str(a)[::-1],str(b)[::-1])]))
