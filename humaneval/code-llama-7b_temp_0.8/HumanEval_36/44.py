

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Count number of times 7 appears in numbers that are divisible by 11 or 13
    # Using the observation that 11 % 7 = 0
    # and 13 % 7 = 5
    count = 0
    for i in range(n):
        if (i % 11) % 7 == 0 or (i % 13) % 7 == 0:
            count += 1
    return count

