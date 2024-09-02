

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    """
    Assuming n is positive and that it is not a power of 10, there will be some non-negative integer less
    than n which is divisible by both 11 and 13. So it suffices to find this number (call it m) and to
    determine the number of times the digit 7 appears in m.
    """
    m = 0
    while (m + 1) % 11 != 0:
        m += 1
    while (m + 1) % 13 != 0:
        m += 1
    count = 0
    while m > 0:
        if m % 10 == 7:
            count += 1
        m //= 10
    return count
