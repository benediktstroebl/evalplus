

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # Define a list of prime numbers that are less than n
    primes = [p for p in range(2, int(n**0.5) + 1) if not n % p]
    # If n is prime, return n
    if n == 1:
        return 1
    # If n is composite and greater than the largest prime in primes, return the largest prime in primes
    elif n > max(primes):
        return max(primes)
    # Otherwise, check if n is divisible by any of the elements in primes
    else:
        for p in primes:
            if n % p == 0:
                return p
        # If no divisor is found, return 1 (this is the largest number that divides n evenly and is smaller than n)
        return 1