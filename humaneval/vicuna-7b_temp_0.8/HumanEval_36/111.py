

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Create an empty list to store the results
    results = []
    
    # Loop through the numbers 1 to n
    for i in range(1, n+1):
        # Check if the number is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # If so, append "Fizz" to the list of results
            results.append("Fizz")
        elif i % 3 == 0:
            # If so, append "Buzz" to the list of results
            results.append("Buzz")
        else:
            # If neither of the above, append the number itself to the list of results
            results.append(i)
    
    # Return the list of results
    return results
