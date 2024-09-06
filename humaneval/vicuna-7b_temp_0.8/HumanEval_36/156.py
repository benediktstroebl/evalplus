

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize variables to keep track of number of times each number appears
    # and which digits are in the sequence.
    return sum(1 for i in range(1, n + 1) if (i % 11 == 0 and i % 13 == 0) or (i % 11 == 1 and i % 13 == 0) or (i % 11 == 0 and i % 13 == 1) or (i % 11 == 1 and i % 13 == 1) or (i % 11 == 1 and i % 13 == 2) or (i % 11 == 2 and i % 13 == 1) or (i % 11 == 2 and i % 13 == 2) or (i % 11 == 3 and i % 13 == 1) or (i % 11 == 3 and i % 13 == 2) or (i % 11 == 4 and i % 13 == 1) or (i % 11 == 4 and i % 13 == 2) or (i % 11 == 6 and i % 13 == 1) or (i % 11 == 6 and i % 13 == 2) or (i % 11 == 6 and i % 13 == 3) or (i % 11 == 6 and i % 13 == 4))
