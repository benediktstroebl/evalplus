

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 0:
        return 0
    if n < 11:
        return 0
    result = 0
    if n % 11 == 0:
        result += fizz_buzz(n // 11)
    if n % 13 == 0:
        result += fizz_buzz(n // 13)
    s = str(n)
    if "7" in s:
        result += s.count("7")
    return result
