

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def fizzbuzz(n):
        if n % 11 == 0:
            return 1 + fizzbuzz(n // 11)
        elif n % 13 == 0:
            return 1 + fizzbuzz(n // 13)
        elif n % 7 == 0:
            return 1 + fizzbuzz(n // 7)
        elif n % 11 == 0:
            return 1 + fizzbuzz(n // 11)
        elif n % 13 == 0:
            return 1 + fizzbuzz(n // 13)
        else:
            return 0
    return fizzbuzz(n)
