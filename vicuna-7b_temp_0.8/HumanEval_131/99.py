
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even, return 0
    if (n % 2 == 0) == len(str(n)):
        return 0
    
    # Otherwise, return the product of the odd digits
    prod = 1
    for i in range(len(str(n))-1):
        if (n // 10) % 2 == 1:
            prod *= 10
        n //= 10
    return prod
