

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize the accumulator to zero.
    count = 0

    # Iterate over the integers in the range from 0 to n, inclusive, by 12's.
    for current_number in range(0, n + 1, 12):
        # If the number is divisible by 11, increment count.
        if current_number % 11 == 0:
            count += 1
        # If the number is divisible by 13, increment count.
        elif current_number % 13 == 0:
            count += 1

    return count
