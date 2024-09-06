

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for n being 0 or 1, which have no divisors
    if n == 0 or n == 1:
        return 0
    # Initialize a counter for each divisor
    fizz = 0
    buzz = 0
    # Check for each divisor
    for i in range(1, n + 1):
        # If the number is divisible by 11, it is also divisible by 2 and 13
        if n % i == 0:
            if i == 11:
                fizz += 1
            elif i == 13:
                buzz += 1
            else:
                fizz += 1
        # If the number is divisible by 13, it is also divisible by 11 and 7
        elif n % i == 0:
            if i == 11:
                fizz += 1
            elif i == 7:
                buzz += 1
            else:
                fizz += 1
        # If the number is divisible by 2, it is also divisible by 3 and 5
        elif n % 2 == 0:
            if i == 3:
                fizz += 1
            elif i == 5:
                fizz += 1
            else:
                fizz += 1
    # Return the correct number of 7's
    return 3 * (fizz - buzz) + 3
