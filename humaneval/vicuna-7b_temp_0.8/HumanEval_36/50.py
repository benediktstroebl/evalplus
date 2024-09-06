

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize an empty list
    results = []
    
    # Iterate over the numbers less than n
    for i in range(1, n):
        # If the number is divisible by 11 or 13, add 7 to the results list
        if i % 11 == 0 or i % 13 == 0:
            results.append(7)
        # If the number is divisible by 3, add 6 to the results list
        elif i % 3 == 0:
            results.append(6)
        # If the number is divisible by 5, add 1 to the results list
        elif i % 5 == 0:
            results.append(1)
        # Otherwise, add the number itself to the results list
        else:
            results.append(i)
    
    return results
