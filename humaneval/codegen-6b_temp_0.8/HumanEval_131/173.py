
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return int(''.join(str(int(i)) for i in str(n) if int(i) % 2 == 1))
    """
    # Using slices and the modulus operator:
    return reduce(lambda x, y: x*y, [int(x) for x in str(n) if int(x) % 2 == 1])
    """
    
