

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Define a helper function to check the remainder of n divided by 11
    def check_remainder(n: int, remainder: int):
        """Return True if n is divisible by 11, False otherwise."""
        return remainder == 0
    
    # Define a helper function to check the remainder of n divided by 13
    def check_remainder(n: int, remainder: int):
        """Return True if n is divisible by 13, False otherwise."""
        return remainder == 0
    
    # Initialize a variable to store the number of 7s in the output
    num_7s = 0
    
    # Iterate through the numbers less than n
    for i in range(1, n + 1):
        # If n is divisible by 11, 13, or 100
        if (n % 11 == 0 or n % 13 == 0 or n % 100 == 0) and check_remainder(n, i):
            # If the number is divisible by 7 or 11 but not 13
            if (i % 7 == 0 or i % 11 == 0) and not check_remainder(i, 13):
                # Add 2 to the number of 7s
                num_7s += 1
        
    # Return the number of 7s in the output
    return num_7s