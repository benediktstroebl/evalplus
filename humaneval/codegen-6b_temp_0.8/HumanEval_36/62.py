

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    n -= 1
    hundred = n // 100
    thousand = (n - hundred * 100) // 1000
    counter = 0
    while hundred:
        if n % 11 == 0 or n % 13 == 0:
            counter += 1
        n -= 1
        hundred -= 1
        n //= 10
    return counter + thousand

