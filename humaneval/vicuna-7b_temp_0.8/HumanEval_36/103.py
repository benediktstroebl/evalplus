

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Compute the first missing digit
    missing = [7] + [fizz[i] for i in range(n) if fizz[i] == 0] + [buzz[i] for i in range(n) if buzz[i] == 0]
    return sum(1 for i in range(n) if missing[i] == 7)
