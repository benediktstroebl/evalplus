

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    n -= 1
    total = 0
    while n >= 0:
        if (n + 1) % 13 == 0:
            if (n + 1) % 11 == 0:
                total += 1
        elif n % 11 == 0:
            total += 1
        n -= 1
    return total

