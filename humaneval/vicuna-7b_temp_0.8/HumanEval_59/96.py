

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    # Return 1 if n is prime
    if n == 1 or n % 2 == 0:
        return n
    
    # Check for cases where n is a prime
    if n > 3:
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return 1
        
        return n
    
    # Check for cases where n is a product of two primes
    if n > 2:
        for i in range(2, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                j = int(n / i)
                if j * j == n:
                    return j
        return n
    
    # Return 1 if n is not a prime or a product of two primes
    return 1
