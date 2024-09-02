

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    number = 7
    max_n = n
    count = 0
    for i in range(n):
        if (i + 1) % number == 0:
            max_n -= number
            count += 1
        if (i + 1) % 3 == 0:
            number = 3
        elif (i + 1) % 5 == 0:
            number = 5
    return count
