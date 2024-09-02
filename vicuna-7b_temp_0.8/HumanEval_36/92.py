

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # If n is 0 or 1, we get 0 or 1.
    if n == 0 or n == 1:
        return n

    # If n is divisible by 11 or 13, we get 7 or 13.
    if n % 11 or n % 13 == 0:
        return n

    # If n has a 7 in it, we get 2.
    for i in range(1, n // 13):
        if n % i == 7:
            return n

    # If n has a 3 in it, we get 3.
    for i in range(1, n // 5):
        if n % i == 3:
            return n

    # If n does not have a 7 or a 3 in it, we get 0.
    return 0
