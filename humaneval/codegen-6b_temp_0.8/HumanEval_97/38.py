
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
    # Your code here
    # The number of digits in each number
    n = len(str(a))
    # convert each to n digits
    a = 10 ** (n-1) * int(str(a)[-1]) + multiply(int(str(a)[:-1]), b)
    b = 10 ** (n-1) * int(str(b)[-1]) + multiply(int(str(b)[:-1]), a)
    return a * b 
