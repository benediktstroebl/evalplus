
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

    def getDigit(n):
        return (n % 10)
    
    def product(n1, n2):
        if n1 == 0 or n2 == 0:
            return 0
        return getDigit(n1) * getDigit(n2)
    
    return product(a, b)

