
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # Use a helper variable to keep track of the remaining digits
    # and check if all digits are even
    digits = 0
    for i in range(n):
        digits = (digits * 10) + (n % 10)
        n = (n // 10)
    return digits % 10
