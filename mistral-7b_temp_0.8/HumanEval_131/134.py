
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    if not n:
        return n
    else:
        a = n % 10
        if a % 2 == 0:
            n = int(n / 10)
            return digits(n)
        else:
            n = int(n / 10)
            return digits(n) * a
