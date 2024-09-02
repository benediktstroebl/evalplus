
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use recursion with an additional base case
    if n < 2:
        return n
    if n % 2 != 0:
        return n // 2
    return n * digits(n // 2)
