

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a variable to keep track of the count of 7
    count = 0
    
    # Loop through the range of numbers from 1 to n
    for i in range(1, n+1):
        # If the number is divisible by 11, increment the count of 7
        if i % 11 == 0:
            count += 1
        # If the number is divisible by 7, increment the count of 1
        if i % 7 == 0:
            count += 1
        # If the number is divisible by 3, increment the count of 3
        if i % 3 == 0:
            count += 3
        
    # Return the count of 7
    return count