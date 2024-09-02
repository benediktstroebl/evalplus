
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Avoid multiplying with the string directly
    digits = '0123456789'
    n = abs(n)

    if n % 2 == 0:
        return 0

    product = 1
    for i in range(1, n):
        product *= int(digits[n // 2])
        n //= 2

    return product
