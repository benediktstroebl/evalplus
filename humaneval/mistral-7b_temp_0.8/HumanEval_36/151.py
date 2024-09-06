

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def divisible_by_11(x: int) -> bool:
        return x % 11 == 0

    def divisible_by_13(x: int) -> bool:
        return x % 13 == 0

    count = 0
    for i in range(2, n):
        if (divisible_by_11(i) or divisible_by_13(i)) and (str(i).count("7") == 2):
            count += 1
    return count

