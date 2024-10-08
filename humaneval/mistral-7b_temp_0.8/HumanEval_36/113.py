

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
    count = 0
    while n >= 1:
        if (n % 11) == 0 or (n % 13) == 0:
            if n % 10 == 7:
                count += 1
        n -= 1
    return count

