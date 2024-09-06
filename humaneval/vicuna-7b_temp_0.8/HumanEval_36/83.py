

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Initialize a list to store the number of times each digit appears
    count = []
    for i in range(1, n+1):
        if i % 11 == 0:
            count.append(1)
        elif i % 13 == 0:
            count.append(1)
        else:
            count.append(0)
        
    # Initialize an empty list to store the number of times 7 appears
    result = []
    
    # Loop through the count list and add 1 to each count for 7
    for c in count:
        if c == 1:
            result.append(7)
        else:
            result.append(c)
    
    return result
