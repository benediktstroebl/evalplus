

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize the result list
    result = []
    
    # Loop through the numbers less than n and check if they are divisible by 11 or 13
    for i in range(1, n+1):
        if i % 11 == 0:
            result.append(i)
        elif i % 13 == 0:
            result.append(i)
        else:
            result.append(i)
            
    # Return the result
    return result