

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for num in range(1, n+1):
        if num % 3 == 0 and num % 5 == 0:
            count += 1
        elif num % 3 == 0:
            count += 1
        elif num % 5 == 0:
            count += 1
    return count
