

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a variable for the number of times digit 7 appears
    digit7 = 0
    
    # Loop through the numbers less than n which are divisible by 11 or 13
    for i in range(1, n + 1):
        # If the number is divisible by 11, it is also divisible by 13
        if i % 11 == 0:
            digit7 += 1
            if i % 13 == 0:
                digit7 += 1
        else:
            digit7 += 1
    
    return digit7
