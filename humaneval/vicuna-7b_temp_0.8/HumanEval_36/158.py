

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Let's use a counting sequence for the digits: 1, 1, 2, 1, 3, 2, 1, 4, 3, ...
    # We can use this to keep track of the number of times 7 appears in the sequence.
    # Counting_sequence = [1, 1, 2, 1, 3, 2, 1, 4, 3]
    count = 1
    for i in range(n):
        remainder = 11 % i % 3 == 0
        count *= 3 ** (remainder // 2)
    return count
