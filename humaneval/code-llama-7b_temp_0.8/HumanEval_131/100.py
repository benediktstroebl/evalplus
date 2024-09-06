
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    # 1. Multiply the digits that are odd.
    # 2. Go digit by digit,
    #      if digit is even, stop.
    #      if digit is odd, multiply it and continue.
    # 3. Return the result
    result = 1
    while n > 0:
        digit = n % 10
        if digit % 2 == 0:
            return 0
        else:
            result = result * digit
        n = n // 10

    return result


