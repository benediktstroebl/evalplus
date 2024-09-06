
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
    
    def toDigits(n):
        return [int(c) for c in str(abs(n))]

    def toNumber(ds):
        n = 0
        for d in ds:
            n = 10 * n + d
        return n

    # your code here
    a = toDigits(a)
    b = toDigits(b)
    return toNumber([a[-1] * b[-1]])
