
def digits(n):
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    digits(1)  == 1
    digits(4)  == 0
    digits(235) == 15
    """
    result = 1
    while n > 0:
        last_digit = n % 10
        result *= last_digit
        n //= 10
    return result

    # Alternative 1
    # return functools.reduce(lambda a, b: a * b, (int(d) for d in str(n) if d != '0'))
    # Alternative 2
    # return functools.reduce(lambda a, b: a * b, (int(d) for d in str(n) if d != '0' and int(d) % 2 == 1))

