
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # this is the same as digits(n//2) + digits(n%2)
    # or, more generally, digits(n//2**i) + digits(n%2**i)
    # this avoids overflows by only using the lower bits
    # of n to compute the digits
    if n > 0:
        return (digits(n//2) + digits(n%2)) % 10
    else:
        return 0
