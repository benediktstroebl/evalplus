

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    fizz = 0
    buzz = 0
    for i in range(1, n + 1):
        divisible_by_7 = (i % 7 == 0)
        divisible_by_11 = (i % 11 == 0)
        divisible_by_13 = (i % 13 == 0)
        if divisible_by_7 or divisible_by_11 or divisible_by_13:
            fizz = fizz + 1
    return fizz

