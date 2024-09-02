

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    fizz = lambda x: x % 11 == 0
    buzz = lambda x: x % 13 == 0
    fizzbuzz = lambda x: fizz(x) and buzz(x)

    count = 0
    for i in range(1, n):
        if fizz(i) or buzz(i) or fizzbuzz(i):
            count += 1
    return count
