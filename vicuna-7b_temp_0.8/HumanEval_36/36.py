

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Loop over all numbers less than n that are divisible by 11 or 13.
    for i in range(1, n + 1):
        # If the number is divisible by 11 or 13, print 7 and increment a counter.
        if i % 11 == 0 or i % 13 == 0:
            fizz_counter += 1
            fizz_buzz_counter += 1
        else:
            # If the number is not divisible by 11 or 13, print the number and increment a counter.
            print(i, end='')
            buzz_counter += 1
    # Print the total number of 7s and buzzes.
    print(fizz_counter)
    print(fizz_buzz_counter)
