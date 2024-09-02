

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    def count_7(n):
        return n.count(7)

    divisible_by_11 = lambda n: n % 11 == 0
    divisible_by_13 = lambda n: n % 13 == 0

    divisible_by_11_or_13 = lambda n: divisible_by_11(n) or divisible_by_13(n)

    return count_7(filter(divisible_by_11_or_13, range(1, n)))

