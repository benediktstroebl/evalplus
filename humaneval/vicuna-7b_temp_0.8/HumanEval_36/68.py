

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for divisibility by 11, 13, and 7
    if n % 11 == 0:
        return 0
    elif n % 13 == 0:
        return 0
    elif n % 7 == 0:
        return 1
    elif n % 11 == 0:
        return 1
    elif n % 13 == 0:
        return 1
    else:
        # Check for divisibility by 11 and 13 in reverse order
        return sum(1 for x in range(n // 13, n // 11 + 1) if n % x == 0)