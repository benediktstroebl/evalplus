
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    digits = [i for i in digits if i % 2 == 1]
    return 0 if len(digits) == 0 else reduce(lambda x, y: x*y, digits)
