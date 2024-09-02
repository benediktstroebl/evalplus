
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    n = int(n)
    if n < 0:
        raise ValueError("n must be positive")
    elif n < 10:
        return n
    else:
        product = 1
        for digit in str(n):
            digit = int(digit)
            if digit % 2:
                product *= digit
        return product

