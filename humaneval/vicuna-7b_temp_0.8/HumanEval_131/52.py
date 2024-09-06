
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # If all digits are even, return 0
    if n % 2 == 0:
        return 0
    # If last digit is odd, return the last odd digit
    if n % 2 == 1:
        return n
    # If none of the above cases hold, return 0
    if n == 0:
        return 0
    # If it's not the first digit, return the product of the digits
    # ignoring the first digit
    return (n // 10) * digits(n % 10)
