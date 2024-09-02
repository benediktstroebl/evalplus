

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    for i in range(n):
        if n % 11 == 0:
            print(i, end=' ')
        if n % 13 == 0:
            print(i, end=' ')
        if n % 7 == 0:
            print(i, end=' ')
        if n % 3 == 0:
            print(i, end=' ')
        elif n % 3 == 1:
            print(i, end=' ')
        if n % 5 == 0:
            print(i, end=' ')
