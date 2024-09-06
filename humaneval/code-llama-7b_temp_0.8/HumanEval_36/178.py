

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    ans = 0
    for i in range(n):
        num = i + 1
        if num % 11 == 0 or num % 13 == 0:
            s = str(num)
            ans += s.count("7")
    return ans

