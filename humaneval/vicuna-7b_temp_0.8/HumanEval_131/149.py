
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 255 is the maximum value for an int in Python 2.x
    # (Python 3.0+ uses a 64-bit int, which is too large for this purpose)
    if n > 255:
        return 0
    digits = [int(n % 10) for _ in range(len(str(n))) if n % 10 != 0]
    if not digits:
        return 0
    return sum(digits)
