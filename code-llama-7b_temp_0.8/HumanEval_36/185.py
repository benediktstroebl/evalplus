

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    divisible_by_11_or_13 = lambda n: (n % 11 == 0 or n % 13 == 0)
    return sum(1 for i in range(n) if divisible_by_11_or_13(i) and '7' in str(i))

