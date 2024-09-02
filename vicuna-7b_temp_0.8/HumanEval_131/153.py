
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check for special case of all even digits
    if sum(map(int,str(n))) % 2 == 0:
        return 0
    # Extract the odd digits
    n = n % 10
    # Compute the product
    while n > 0:
        n = n // 10
        product = product * 10 + (n % 10)
    return product
