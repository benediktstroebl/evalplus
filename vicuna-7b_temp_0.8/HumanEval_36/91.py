

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # base case
    if n <= 1:
        return 0
    
    # if the number is divisible by 7, return 7
    if n % 7 == 0:
        return 7
    
    # if the number is divisible by 11, return the number of times 7 appears in the number
    if n % 11 == 0:
        return fizz_buzz(n // 11)
    
    # if the number is 3, we don't know what to do
    if n == 3:
        return 0
    
    # if the number is divisible by 13, return the number of times 7 appears in the number
    if n % 13 == 0:
        return fizz_buzz(n // 13)
    
    # if the number is not divisible by 7 or 11, we don't know what to do
    # so return 0
    return 0