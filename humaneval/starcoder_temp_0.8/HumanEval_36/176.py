

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(1, n):
        if is_divisible_by(i, 11):
            count += 1
        elif is_divisible_by(i, 13):
            count += 1
    return count
