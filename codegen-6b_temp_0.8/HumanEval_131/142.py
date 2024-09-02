
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all numbers are even, return 0.
    if n < 1:
        return 0

    total = 1
    while n > 0:
        i = n % 10
        # Skip the evens.
        if i % 2 == 0:
            n = n // 10
            continue
        total = total * i
        n = n // 10

    return total

