

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # if n < 11:
    #     return 0
    # if n % 11 != 0 and n % 13 != 0:
    #     return 0
    # return (n // 11) + (n // 13)
    return sum(1 for i in range(1, n) if i % 11 == 0 or i % 13 == 0 and str(i).__contains__("7"))

