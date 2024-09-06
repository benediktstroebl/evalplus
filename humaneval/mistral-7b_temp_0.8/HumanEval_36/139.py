

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if not isinstance(n, int):
        raise TypeError('n must be an integer')

    def is_divisible_by_11(n):
        return n % 11 == 0

    def is_divisible_by_13(n):
        return n % 13 == 0

    def is_divisible_by_7(n):
        return n % 7 == 0

    def is_digit_7(n):
        return str(n)[-1] == '7'

    def find_7_in_fizz_buzz(n):
        count = 0
        for i in range(2, n):
            if (is_divisible_by_11(i) or is_divisible_by_13(i)) and is_divisible_by_7(i):
                count += 1
        return count

    if n <= 0:
        return 0

    return find_7_in_fizz_buzz(n)

