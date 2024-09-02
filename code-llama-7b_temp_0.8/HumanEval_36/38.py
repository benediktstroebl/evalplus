

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    def is_divisible(i: int, x: int):
        return i % x == 0

    def has_seven(i: int):
        return str(i).count("7") > 0

    count = 0
    for i in range(1, n):
        if has_seven(i) and (is_divisible(i, 11) or is_divisible(i, 13)):
            count += 1
    return count

