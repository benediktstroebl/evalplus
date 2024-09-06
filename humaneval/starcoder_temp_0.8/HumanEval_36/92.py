

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def is_11_or_13_divisible(x: int):
        return x % 11 == 0 or x % 13 == 0
    def count_7s(x: int):
        return str(x).count("7")
    return sum(count_7s(x) for x in range(1, n) if is_11_or_13_divisible(x))
