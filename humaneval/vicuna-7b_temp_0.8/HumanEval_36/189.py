

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Start at 1 and check divisibility by 3
    count = 1
    for i in range(1, n+1):
        if i % 3 == 0:
            count += 1
    # Add count of 7s for divisibility by 11
    count += 1 if (n % 11) == 0 else 0
    # Check if n is divisible by 13 and increment count if so
    count += 1 if (n % 13) == 0 else 0
    return count
