

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Hint: Instead of trying to list all numbers below n which are divisible by 11 or 13,
    # you can try to understand the numbers that are not divisible by 11 or 13.

    num = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            num += 1
        if i % 7 == 0:
            num -= 1
    return num
