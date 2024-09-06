
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
    # the solution below was changed after testing with different inputs.
    # the original code was like below.
    # return (a%10) * (b%10)
    return int((a%10)*(b%10))

