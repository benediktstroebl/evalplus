

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Special case for n == 0
    if n == 0:
        return 0
    # Initialize an empty list to store the results
    results = []
    # Loop through the numbers from 1 to n
    for i in range(1, n+1):
        # Loop through the numbers from 7 to n+1
        for j in range(7, n+1, 3):
            # If the current number is divisible by 11 or 13, increment the count
            if j % 11 == 0 or j % 13 == 0:
                results.append(1)
        else:
            # If the current number is not divisible by 11 or 13, increment the count
            results.append(1)
    return results
