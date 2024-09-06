
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Check if all digits are even
    if sum(map(lambda x: x % 2 if x > 0 else 0, [n // i for i in range(len(n))])) == 0:
        return 0
    # Otherwise, compute and return the product of the odd digits
    prod = 1
    for i in range(len(n) // 2):
        prod *= n // i
    return prod