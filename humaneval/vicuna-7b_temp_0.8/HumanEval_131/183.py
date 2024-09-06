
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # We can use the fact that the sum of digits in base 10 is 10, and
    # if the number is divisible by 3, the sum of digits in the last two
    # digits is 1.
    if n % 3 == 0:
        return 0
    result = 0
    for i in range(1, 10):
        if n % i == 0:
            if n // i == 2:
                # We have two consecutive digits that are different and odd.
                result = result * i
            else:
                # We have an odd digit and the next digit is different.
                result = result * i + n // i
        else:
            result = result * i
    return result
