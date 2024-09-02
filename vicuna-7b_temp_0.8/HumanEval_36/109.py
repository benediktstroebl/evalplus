

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a variable to store the count of 7
    count = 0
    
    # Loop through the integers less than n
    for i in range(1, n):
        # Check if the integer is divisible by 11
        if i % 11 == 0:
            # Check if the integer is divisible by 7
            if i % 7 == 0:
                # Increment the count of 7
                count += 1
            elif i % 3 == 0:
                # Increment the count of 3
                count += 1
        # Check if the integer is divisible by 13
        elif i % 13 == 0:
            # Check if the integer is divisible by 3
            if i % 3 == 0:
                # Increment the count of 3
                count += 1
            elif i % 5 == 0:
                # Increment the count of 5
                count += 1
        # If none of the above conditions are met, increment the count of 7
        elif i % 7 != 0:
            count += 1
    
    return count
