

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize the count of fizzbuzz patterns
    count = 0
    # Loop through the numbers less than n
    for i in range(1, n):
        # Loop through the numbers from 11 to 13
        for x in range(11, 14):
            # If the number is divisible by 11 and x, the number is divisible by 11
            if i % x == 0:
                # If the number is divisible by 13, the number is divisible by x
                if i % 13 == 0:
                    count += 1
    return count
