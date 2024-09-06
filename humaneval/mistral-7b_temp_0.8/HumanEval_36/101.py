

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def helper(n: int):
        """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
        >>> helper(50)
        0
        >>> helper(78)
        2
        >>> helper(79)
        3
        """
        return 0 if n == 1 else helper(n - 1) + (1 if n % 11 == 0 or n % 13 == 0 else 0) * (n % 10 == 7)
    return helper(n - 1)

