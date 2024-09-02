

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # check if n is a prime
    if n > 1 and n % 2 == 0:
        return 2
    
    # check if n is divisible by 3
    if n > 1 and n % 3 == 0:
        return 3
    
    # check if n is divisible by 4
    if n > 1 and n % 4 == 0:
        return 4
    
    # check if n is divisible by 5
    if n > 1 and n % 5 == 0:
        return 5
    
    # check if n is divisible by 6
    if n > 1 and n % 6 == 0:
        return 6
    
    # keep track of the largest prime factor found
    largest = 2
    while n > 1:
        # check if n is divisible by the current prime factor
        if n % largest == 0:
            return largest
        # increment the largest prime factor found
        largest += 2
    # if no prime factor was found, return 2
    return 2
