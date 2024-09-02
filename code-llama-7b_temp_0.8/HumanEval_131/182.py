
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 0:
        n = -n

    odd_digits = []

    while n:
        n, digit = divmod(n, 10)
        if digit % 2 == 1:
            odd_digits.append(digit)
    return product(odd_digits)

