
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Product of odd numbers
    prod = 1
    # i is the current digit
    i = n % 10
    # n is the number
    while n > 0:
        if i % 2 != 0:
            prod *= i
        i = n % 10
        n = n // 10
    return prod

