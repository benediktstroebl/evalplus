
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    def helper(n):
        if n // 10 == 0:
            return n
        a, b = n // 10, n % 10
        if b % 2 != 0:
            return (a * b) + helper(a)
        else:
            return helper(a)

    # helper(n) returns the product of the odd digits of n
    # invalid inputs, e.g. n < 100
    return helper(n)

