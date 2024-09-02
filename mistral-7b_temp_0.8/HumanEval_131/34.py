
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Your code here
    odd_digits = 1
    if n < 10:
        return 0
    while n > 0:
        if n % 10 % 2 == 1:
            odd_digits *= n % 10
        n //= 10
    return odd_digits
