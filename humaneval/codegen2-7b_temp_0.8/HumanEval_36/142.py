

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum(
        digit in (7,11,13) and (digit * digit) % n == 0
        for digit in range(1, int(math.sqrt(n))+1)
    
