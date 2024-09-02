

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Using a variable to store the number of times the digit 7 appears
    num_7 = 0
    
    # Using a variable to store the number of times the digit 13 appears
    num_13 = 0
    
    # Using a variable to store the number of times the digit 11 appears
    num_11 = 0
    
    # Iterating over the integers from 1 to n
    for i in range(1, n + 1):
        
        # If the number is divisible by 7 or 13
        if i % 11 == 0 or i % 13 == 0:
            
            # Increment the number of times the digit 7 appears
            num_7 += 1
            
        # Increment the number of times the digit 13 appears
        num_13 += 1
        
        # Increment the number of times the digit 11 appears
        num_11 += 1
        
    # Returning the number of times the digit 7 appears
    return num_7