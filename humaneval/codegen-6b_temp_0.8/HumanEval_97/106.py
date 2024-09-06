
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
    # http://www.geeksforgeeks.org/multiplication-of-digits-in-a-number-in-python/
    # print(*(a%b for i in range(1, abs(b))))
    # print(*(a//b for i in range(abs(b))))
    # print(a,b,a%b,a//b)
    # a = abs(a)
    # b = abs(b)
    # temp = 0
    # for i in range(b):
    #     temp += a%10 * (10**i)
    # return temp