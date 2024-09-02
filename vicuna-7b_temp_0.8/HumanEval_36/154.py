

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check if n is divisible by 11 and 13
    if n % 11 == 0 and n % 13 == 0:
        # n is divisible by 11 and 13, so return 0
        return 0
    # Check if n is divisible by 3
    if n % 3 == 0:
        # n is divisible by 3, so return 1
        return 1
    # Check if n is divisible by 5
    if n % 5 == 0:
        # n is divisible by 5, so return 2
        return 2
    # Check if n is divisible by 7
    if n % 7 == 0:
        # n is divisible by 7, so return 3
        return 3
    # If n is not divisible by any of the above, return the number of times the digit 7 appears
    # in the numbers from 1 to n (which are also divisible by 7)
    return 7 * (n // 7)
