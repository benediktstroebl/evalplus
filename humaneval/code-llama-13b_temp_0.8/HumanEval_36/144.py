

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Hint:
    # to check if a number is divisible by 11 or 13, do the following:
    # divisor % (11 or 13) == 0
    # for example, check if 24 is divisible by 13:
    # 24 % 13 == 0
    # and this can be applied to any number, not just 24.
    count = 0
    for i in range(1, n):
        if i % (11 or 13) == 0:
            i = str(i)
            if '7' in i:
                count += 1
    return count
