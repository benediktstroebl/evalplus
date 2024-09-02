
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
    #1. convert both numbers to string
    a = str(a)
    b = str(b)
    #2. take the unit digits of both numbers
    #3. convert both numbers to int
    #4. multiply both numbers and return the result
    a = int(a[len(a)-1])
    b = int(b[len(b)-1])
    return a*b

