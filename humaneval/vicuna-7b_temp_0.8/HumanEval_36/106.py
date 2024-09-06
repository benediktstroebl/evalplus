

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize variable
    count = 0
    
    # Loop through the numbers less than n
    for i in range(1, n + 1):
        # Check if the number is divisible by 11
        if i % 11 == 0:
            # Check if the number is divisible by 13
            if i % 13 == 0:
                # If both are true, increment the count
                count += 1
            # If either is true, increment the count
            elseif i % 13 == 0:
                count += 2
            # If neither is true, increment the count
            else:
                count += 1
    
    # Return the count
    return count
