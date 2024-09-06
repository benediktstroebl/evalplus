

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    div_by_11 = 0
    div_by_13 = 0

    for i in range(n):
        # check if number is divisible by 11
        if i % 11 == 0:
            div_by_11 += 1

        # check if number is divisible by 13
        if i % 13 == 0:
            div_by_13 += 1

    return div_by_11 + div_by_13

