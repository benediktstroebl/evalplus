
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def bits(n):
        "Generate an iterable of the bits of n as an int."
        while n:
            yield n & 1
            n >>= 1

    prod = 1
    for i in bits(n):
        prod *= i
    return prod
