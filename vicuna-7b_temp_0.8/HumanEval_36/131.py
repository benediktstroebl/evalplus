

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a dictionary to store the counts of the number of times the digits 11 and 13 appear
    fizz_buzz_count = {
        11: 0,
        13: 0,
        7: 1
    }
    # Loop through the numbers less than n
    for i in range(1, n):
        # Check if the number is divisible by 11
        if i % 11 == 0:
            fizz_buzz_count[11] += 1
        # Check if the number is divisible by 13
        if i % 13 == 0:
            fizz_buzz_count[13] += 1
        # Check if the number is divisible by 7
        if i % 7 == 0:
            fizz_buzz_count[7] += 1
    return fizz_buzz_count[7]