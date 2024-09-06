

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check if the number is divisible by 11 or 13
    if n % 11 or n % 13:
        # Check if the number is divisible by 7
        return n % 7
    # If none of the above, return 0
    return 0
