

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    total = 0
    for i in range(1, n):
        if is_divisible(i, 7) and is_divisible(i, 11) or is_divisible(i, 13):
            total += 1
    return total
