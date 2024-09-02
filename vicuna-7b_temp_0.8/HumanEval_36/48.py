

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize variables
    total = 0
    fizz = 0
    buzz = 0
    
    # Check all numbers less than n
    for i in range(1, n+1):
        # Check if the number is divisible by 11
        if i % 11 == 0:
            # If it is divisible by both 11 and 13, increment both fizz and buzz
            if i % 13 == 0:
                fizz += 1
                buzz += 1
        # If the number is divisible by 7, increment the total variable
        elif i % 7 == 0:
            total += 1
    
    # Return the result
    return total
