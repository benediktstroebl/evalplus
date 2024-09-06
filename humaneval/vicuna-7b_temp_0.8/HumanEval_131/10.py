
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not (n % 2 == 0):
        return n
    digits = []
    for i in range(1, len(str(n))):
        digit = int(n % 10)
        digits.append(digit)
        n //= 10
        if n == 0:
            return 0
    return sum(digits)
