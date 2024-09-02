

def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
    # Prime numbers are odd numbers with no two digits
    if n % 2 != 0:
        return True
    
    # Check for small numbers that are not prime
    if n < 3:
        return False
    if n == 3:
        return True
    if n == 5:
        return True
    if n % 2 == 0:
        return False
    
    # Generate a list of numbers less than n and check if n is divisible with any of them
    div_list = [2, 3]
    while len(div_list) < n:
        for d in div_list:
            if n % d == 0:
                return False
        div_list.append(n // d)
        
    # The last divisor is n itself, so n is prime
    return True
