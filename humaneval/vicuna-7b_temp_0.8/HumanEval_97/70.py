
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
    return int(sum(int(d) * int(str(b)[1:]) // int(str(a)[1:]) for d in str(a)[1:]))

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = multiply(a, b)
