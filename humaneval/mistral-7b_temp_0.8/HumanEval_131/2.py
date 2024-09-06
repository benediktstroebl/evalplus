
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    return (n % 10) * (n // 10 % 10) * (n // 100 % 10) * (n // 1000 % 10)



