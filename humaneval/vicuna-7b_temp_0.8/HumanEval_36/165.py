

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # if n is 0, return 0 to indicate success
    if n == 0:
        return 0
    
    # create a list of divisors for each divisor of n
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    
    # iterate over the divisors, checking if the number is divisible by 11 or 13 and incrementing the counter if it is
    result = 0
    for d in divisors:
        if n % d == 0:
            result += 1
        elif n % d == 13:
            result += 2
    
    # return the result
    return result
