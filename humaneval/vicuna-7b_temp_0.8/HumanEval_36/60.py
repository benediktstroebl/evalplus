

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for special case 11
    if n % 11 == 0:
        return 1
    # Check for special case 13
    if n % 13 == 0:
        return 1
    # Loop to find the number of times 7 appears
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and n % (i + 7) == 0:
            count += 1
    return count
