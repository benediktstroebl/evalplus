

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize an empty list to store the results
    results = []
    # Check all numbers less than n that are divisible by 11 and 13
    for i in range(1, n + 1):
        if (i % 11) == 0 or (i % 13) == 0:
            results.append(i)
    # Count the number of times 7 appears in the list of results
    return len(filter(lambda x: 7 in str(x), results))
