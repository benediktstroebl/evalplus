

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def fizz_buzz_sequence(n: int):
        a = divisible_by_11(n)
        b = divisible_by_13(n)
        return a + b
    return fizz_buzz_sequence(n) if n > 0 else 0
