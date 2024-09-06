

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Handle the base case
    if n <= 1:
        return 1
    
    # Handle the 7 case
    count = 0
    for i in range(2, n+1):
        if i % 11 == 0:
            count += 1
        elif i % 13 == 0:
            count += 1
        elif i % 7 == 0:
            count += 1
    
    # Handle the rest of the cases
    for i in range(11, n+11):
        if i % 11 == 0:
            count += 1
        elif i % 13 == 0:
            count += 1
    return count
