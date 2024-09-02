
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # optimization: using the same code twice, like a boss
    if n % 2 == 0:
        return 0
    else:
        # determine the number of digits by using the ceiling of log2(n)
        # that is, the number of digits minus 1
        digits = n // (10**(len(str(int(n)))) - 1)
        # check if all digits are odd
        odd_digits = 0
        for i in range(digits):
            if n % 10**i != 0:
                odd_digits += 1
        return odd_digits * 10**(len(str(int(n))) - 1)
