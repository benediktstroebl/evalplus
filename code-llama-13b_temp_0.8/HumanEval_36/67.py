

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
    for i in range(7, n):
        if i % 7 == 0:
            count += 1
            continue
        str_i = str(i)
        if '7' in str_i:
            count += 1

    return count

