

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    def is_divisible(n: int, divisor: int) -> bool:
        """Check whether n is divisible by divisor"""
        return n % divisor == 0

    def count_7s(num: int) -> int:
        """Return the number of 7s in the representation of num, including leading zeros"""
        count = 0
        while num:
            num, digit = divmod(num, 10)
            if digit == 7:
                count += 1
        return count

    result = 0
    for num in range(11, n + 1, 11):
        if is_divisible(num, 13):
            result += count_7s(num)
    return result

