

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum(n % i == 0 and (n % i / i) % 10 not in {7, 5, 3, 11, 13} for i in range(1, n))
