
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    return 1 if n == 1 else 0 if n % 2 == 0 else reduce(
        lambda x, y: x * y,
        [int(x) for x in str(n) if int(x) % 2 == 1],
    )
