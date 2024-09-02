
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Efficient algorithm for large n
    digits = []
    while n:
        if n % 2 != 0:
            digits.append(n % 2)
        n = n // 2
    if all(d == 1 for d in digits):
        return 0
    return 2**len(digits)
