
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
    # def to_digit(n):
    #     return int(str(abs(n))[-1])

    def to_digit(n):
        return n%10

    return to_digit(a)*to_digit(b)
