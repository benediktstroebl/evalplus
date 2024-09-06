

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n >= 100:
        raise ValueError("n must be less than 100")
        
    return sum(divby(n, 7) for n in range(1, n))
