
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

    odd_prod = 1
    while n:
        r = n % 10
        if r % 2 == 1:
            odd_prod = odd_prod * (r)
        n = n // 10
    return odd_prod

