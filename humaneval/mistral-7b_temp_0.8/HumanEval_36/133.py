

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # is_fizz_buzz_num = lambda n: n % 11 == 0 or n % 13 == 0
    # count = 0
    # for n in range(1, n):
    #     if is_fizz_buzz_num(n):
    #         count += 1
    #         if n % 7 == 0:
    #             count += 1
    # return count

    # return sum(1 for n in range(1, n) if n % 11 == 0 or n % 13 == 0 and n % 7 == 0)
    return sum(1 for n in range(1, n) if n % 11 == 0 or n % 13 == 0 and n % 7 == 0)

