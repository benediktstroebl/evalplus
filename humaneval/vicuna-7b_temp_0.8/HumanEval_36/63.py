

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize 7-count variable outside of loop
    7_count = 0
    
    # Iterate over all integers less than n
    for i in range(1, n+1):
        # Check if i is divisible by 7, 11, or 13
        if i % 7 == 0:
            # If i is divisible by 7, increment 7-count
            7_count += 1
        elif i % 11 == 0:
            # If i is divisible by 11, increment 7-count
            7_count += 1
        elif i % 13 == 0:
            # If i is divisible by 13, increment 7-count
            7_count += 1
    
    # Return the 7-count
    return 7_count
