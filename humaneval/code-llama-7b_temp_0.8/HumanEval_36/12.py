

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Imp. 1
    # counts = 0
    # for i in range(n):
    #     if str(i).find("7") != -1:
    #         counts += 1
    #     if i % 11 == 0 or i % 13 == 0:
    #         counts += 1
    # return counts
    # Imp. 2
    # return sum(i.count("7") for i in (str(n - i) for i in range(n)) if i % 11 == 0 or i % 13 == 0)
    # Imp. 3
    return sum(i.count("7") for i in (str(i) for i in range(n)) if i % 11 == 0 or i % 13 == 0)

