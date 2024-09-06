

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    while n > 0:
        if n % 11 == 0:
            fizz = 1
        else:
            fizz = 0
        if n % 13 == 0:
            fizzbuzz = 1
        else:
            fizzbuzz = 0
        if n % 111 == 0:
            fizzbuzz *= 11
        else:
            fizzbuzz *= 13
        n = n // 11

    return fizz, fizzbuzz
