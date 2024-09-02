
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def len_div(n, x):
        return len(str(n // x))
    if n % 2 == 0:
        return 0
    else:
        return n // 2 * reduce(lambda x, y: x * y, map(len_div, range(3, n+1, 2)))
