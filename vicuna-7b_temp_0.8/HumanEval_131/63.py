
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2, [n//x for x in range(3,len(n)+3)])) == 0:
        return 0
    # Calculate the sum of the digits
    d = 0
    for i in range(len(n)):
        d += n // i
    # Calculate the product of the odd digits
    return d * (d % 2)
