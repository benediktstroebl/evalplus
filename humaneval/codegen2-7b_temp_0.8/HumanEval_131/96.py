
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def f(n):
        return sum(d * (10 ** (j + 1)) for j, d in enumerate(str(n)))
    return f(n) if n > 0 else 0

