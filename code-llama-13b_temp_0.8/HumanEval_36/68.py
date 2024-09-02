

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    divisible_by_11 = n % 11 == 0
    divisible_by_13 = n % 13 == 0

    if divisible_by_11 or divisible_by_13:
        return 0

    if n <= 79:
        return 3

    return 3 + fizz_buzz(n - 11) + fizz_buzz(n - 13)
