
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
    
    def digit_multiply(number):
        product = 1
        n = abs(number)
        while n > 0:
            product *= n % 10
            n //= 10
        return product
    
    return digit_multiply(a) * digit_multiply(b)