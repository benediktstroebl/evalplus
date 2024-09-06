
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
    def digit_mul(x):
        return x*digit_mul(x-1) if x else 1
    return sum(digit_mul(a) * digit_mul(b) 
                for d in range(10) if a and b)
