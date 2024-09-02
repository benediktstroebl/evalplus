

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check if n is divisible by 11
    if n % 11 == 0:
        return 0
    
    # Check if n is divisible by 13
    if n % 13 == 0:
        return 0
    
    # If n is not divisible by 11 or 13, it will have at least one digit that is divisible by 3
    fizz = 0
    buzz = 0
    for i in range(1, n):
        # Check if i is divisible by 3
        if i % 3 == 0:
            fizz += 1
        else:
            buzz += 1
    
    # Add the number of times 7 appears in multiples of 11 and 13
    return fizz + buzz + 2