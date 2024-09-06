

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Loop through the numbers less than n which are divisible by 11, 13, or 7.
    # If the number is divisible by 7, we return 7, otherwise we return the number.
    # We keep track of how many times we've returned 7 in the loop variable 'count'.
    # Once the loop finishes, we return 7 - count.
    count = 0
    for i in range(n, 1, -1):
        if i % 7 == 0:
            count += 1
        elif i % 13 == 0:
            count += 1
        elif i % 11 == 0:
            count += 1
        else:
            yield i
