

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # return sum([1 for num in range(1, n) if ((num % 11 == 0) or (num % 13 == 0))])
    return sum([num for num in range(1, n) if fizz_buzz_helper(num)])
