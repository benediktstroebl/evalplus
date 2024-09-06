
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        n = abs(n)

    # base case
    if n == 0:
        return 1
    elif n == 1:
        return 0

    odds = 1

    # multiply odd digits
    while n % 2 == 0:
        n //= 2

    while n != 1:
        if n % 2 == 0:
            n //= 2
            continue
        odds *= n % 10
        n //= 10

    return odds

