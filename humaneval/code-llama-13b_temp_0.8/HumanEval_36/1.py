

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 1st method:
    count = 0
    for i in range(n):
        if i % 7 == 0 and (i % 11 == 0 or i % 13 == 0):
            count += 1
    return count

    # 2nd method:
    return len(
        [i for i in range(n) if i % 7 == 0 and (i % 11 == 0 or i % 13 == 0)]
    )

    # 3rd method:
    # return sum([1 for i in range(n) if i % 7 == 0 and (i % 11 == 0 or i % 13 == 0)])
