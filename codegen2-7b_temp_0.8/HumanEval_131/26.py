
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if n < 2:
        return 0
    even = 0
    odd = 1
    while n > 0:
        if n % 2 == 0:
            even += 1
            n = n / 2
        else:
            odd *= n % 10
            n = (n - n % 10) / 10
    return odd *
