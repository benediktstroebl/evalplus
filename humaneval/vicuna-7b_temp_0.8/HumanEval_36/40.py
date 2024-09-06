

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize an empty list to store the count of 7's
    count7 = []
    # Iterate over the range 1 to n
    for i in range(1, n+1):
        # Check if i is divisible by 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # If it is, increment the count of 7's
            count7.append(count7.append(i) if i % 11 == 0 else i)
    return count7[-1]
