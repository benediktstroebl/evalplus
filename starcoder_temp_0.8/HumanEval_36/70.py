

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    fizz_count = 0
    buzz_count = 0
    for i in range(n):
        if i % 11 == 0:
            fizz_count += 1
        if i % 13 == 0:
            buzz_count += 1

    return fizz_count + buzz_count

