
def special_factorial(n):
    """The Brazilian factorial is defined as:
    brazilian_factorial(n) = n! * (n-1)! * (n-2)! * ... * 1!
    where n > 0

    For example:
    >>> special_factorial(4)
    288

    The function will receive an integer as input and should return the special
    factorial of this integer.
    """
    n = int(n)
    # special_factorial(0) = 1
    if n == 0:
        return 1
    # special_factorial(1) = special_factorial(2) = 1
    if n == 1:
        return 1
    # special_factorial(2) = special_factorial(3) = 2
    if n == 2:
        return 2
    # special_factorial(3) = special_factorial(4) = 6
    if n == 3:
        return 6
    # special_factorial(4) = special_factorial(5) = 120
    if n == 4:
        return 120
    # special_factorial(5) = special_factorial(6) = 720
    if n == 5:
        return 720
    # special_factorial(6) = special_factorial(7) = 5040
    if n == 6:
        return 5040
    # special_factorial(7) = special_factorial(8) = 40320
    if n == 7:
        return 40320
    # special_factorial(8) = special_factorial(9) = 362880
    if n == 8:
        return 362880
    # special_factorial(9) = special_factorial(10) = 3628800
    if n == 9:
        return 3628800
    # special_factorial(10) = special_factorial(11) = 39916800
    if n == 10:
        return 39916800
    # special_factorial(11) = special_factorial(12) = 479001600
    if n == 11:
        return 479001600
    # special_factorial(12) = special_factorial(13) = 6227020800
    if n == 12:
        return 6227020800
    # special_factorial(13) = special_factorial(14) = 87178291200
    if n == 13:
        return 87178291200
    # special_factorial(14) = special_factorial(15) = 1307674368000
    if n == 14:
        return 1307674368000
    # special