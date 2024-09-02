

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a list to store the numbers
    numbers = [0] * n
    
    # Loop through the numbers and mark the divisible ones
    for i in range(1, n):
        if i % 11 == 0:
            numbers[i-1] += 1
        elif i % 13 == 0:
            numbers[i-1] += 2
        elif i % 3 == 0:
            numbers[i-1] += 1
        else:
            numbers[i-1] += 1
    
    # Return the result
    return numbers
