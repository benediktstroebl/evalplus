

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 1:
        return 0
    for i in range(1, n + 1):
        if n % i == 0:
            if n % 11 == 0:
                return fizz_buzz(n // 11) + 1
            if n % 13 == 0:
                return fizz_buzz(n // 13) + 1
        if i % 3 == 0:
            fizz = fizz_buzz(n // 3) + 1
        if i % 5 == 0:
            fizz = fizz_buzz(n // 5) + 1
        if i % 7 == 0:
            buzz = fizz_buzz(n // 7) + 1
    return 0