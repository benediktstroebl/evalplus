

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # My original solution.
    # return sum(1 for i in range(n) if '7' in str(i) and i % 11 in [0, 10, 22] or i % 13 in [0, 10, 14])

    # Martial's solution.
    return sum(int(c) for i in range(n) for c in str(i) if i % 11 in [0, 10, 22] or i % 13 in [0, 10, 14] if '7' in str(i))

