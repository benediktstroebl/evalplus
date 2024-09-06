

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    fizz_buzz_numbers = {
        i for i in range(1, n)
        if 11 * (i // 11) + 13 * (i // 13) == i
    }
    return sum(
        [
            len(str(i)) - len(str(i).replace('7', ''))
            for i in fizz_buzz_numbers
            if i % 11 == 7
        ]
    )

