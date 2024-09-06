
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # ...
    def odds(n):
        return n % 2 == 1

    if n < 10:
        return n
    else:
        return digits(n / 10) * (n % 10 if odds(n) else 1)

