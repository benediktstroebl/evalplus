
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
    # Your code goes here
    # for i in range(10):
    #     if int(a%10) != 0:
    #         a -= int(a%10)
    #     if int(b%10) != 0:
    #         b -= int(b%10)
    #     print(int(a%10) * int(b%10))
    return int(str(a*b)[-1])

