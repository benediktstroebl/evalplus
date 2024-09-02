

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # avoid using range
    n = min(n, 100)
    d = {7: 0, 11: 0, 13: 0}
    result = []
    for i in range(n):
        if i % 11 == 0:
            d[7] += 1
            if i % 13 == 0:
                d[13] += 1
        if d[7] > 0 and d[7] % 2 == 0:
            result.append("FizzBuzz")
            d[7] = 0
        if d[13] > 0 and d[13] % 2 == 0:
            result.append("FizzBuzz")
            d[13] = 0
        if i % 11 == 0:
            d[11] += 1
        if i % 13 == 0:
            d[13] += 1
    result.append("FizzBuzz")
    return result