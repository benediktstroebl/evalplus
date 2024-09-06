
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """

    if n < 10:
        return n
    odd_digits = 0
    for i in str(n):
        if int(i) % 2 == 0:
            return 0
        else:
            odd_digits = odd_digits * int(i)
    return odd_digits
